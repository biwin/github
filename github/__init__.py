import requests


class GitHub(object):
    action = None
    _action = None
    user = None
    BASE_URL = 'https://api.github.com'
    repo = None

    def __init__(self):
        self.headers = {
            "Accept": "application/vnd.github.v3+json"
        }

    def __make_call(self, endpoint, method='GET'):
        if method == 'GET':
            requests.get(endpoint, headers=self.headers)

    @property
    def repositories(self):
        self._action = 'repositories'
        return self

    def __handle_direct_calls(self):
        if not self._action:
            raise ValueError("Method not allowed, Consult Documentation!!")
        self.action = self._action
        self._action = None

    def list(self, user=None, org=False):
        self.__handle_direct_calls()
        if not user:
            user = self.user
        if self.action == 'repositories':
            if not org:
                endpoint = self.BASE_URL + '/users/{username}/repos'.format(username=user)
            else:
                endpoint = self.BASE_URL + '/orgs/{org}/repos'.format(org=user)

    def __handle_repo_path(self, path):
        _repo = path.split('/')
        if len(_repo) == 2:
            return _repo[0], _repo[1]
        elif len(_repo) == 1:
            return self.user, _repo[0]
        # todo get repo path from repo url
        raise ValueError('Repository Path Invalied, it should look like biwin/github and should be a github repo')

    def get(self, repository_path):
        # github.repositories.get('biwin/angular')
        # github.repositories.get('angular')
        self.__handle_direct_calls()
        if self.action == 'repositories':
            owner, repo = self.__handle_repo_path(repository_path)
            endpoint = self.BASE_URL + '/repos/{owner}/{repo}'.format(owner=owner, repo=repo)

    def topics(self, repository_path):
        self.__handle_direct_calls()
        if self.action == 'repositories':
            owner, repo = self.__handle_repo_path(repository_path)
            self.headers['accept'] = 'application/vnd.github.mercy-preview+json'
            endpoint = self.BASE_URL + '/repos/{owner}/{repo}/topics'.format(owner=owner, repo=repo)

    def languages(self, repository_path):
        self.__handle_direct_calls()
        if self.action == 'repositories':
            owner, repo = self.__handle_repo_path(repository_path)
            endpoint = self.BASE_URL + '/repos/{owner}/{repo}/languages'.format(owner=owner, repo=repo)
            print endpoint

    def teams(self, repository_path):
        self.__handle_direct_calls()
        if self.action == 'repositories':
            owner, repo = self.__handle_repo_path(repository_path)
            endpoint = self.BASE_URL + '/repos/{owner}/{repo}/teams'.format(owner=owner, repo=repo)
            print endpoint

    def tags(self, repository_path):
        self.__handle_direct_calls()
        if self.action == 'repositories':
            owner, repo = self.__handle_repo_path(repository_path)
            endpoint = self.BASE_URL + '/repos/{owner}/{repo}/tags'.format(owner=owner, repo=repo)
            print endpoint
