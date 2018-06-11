from collections import namedtuple
import os

from github import Github, InputFileContent

gh = Github()
pb = gh.get_user('pybites')

pb.get_repos()

Repo = namedtuple('Repo', 'name stars forks')


def main():

    status = get_repo_stats(pb)
    token = os.environ['GH_GIST_CREATE_TOKEN']
    gh = Github(token)
    me = gh.get_user()

    code = '''
    from collections import namedtuple

    Repo = namedtuple('Repo', 'name stars forks')
 

    def get_repo_stats(user, n=5):
        """Takes a Github user object and returns the top n most popular repos by star count,
           skips forks."""
        repos = []
        for repo in user.get_repos():
            if repo.fork:
                continue

            repos.append(Repo(name=repo.name,
                              stars=repo.stargazers_count,
                              forks=repo.forks_count))

        return sorted(repos, key=lambda x: x.stars, reverse=True)[:n]
    '''

    me.create_gist(True,
                   {"repo_stats.py": InputFileContent(code)},
                   "Get GH user's most popular repos")



def get_repo_stats(user, n=5):
    """We did this exercise in our own 100 Days of Code:
       https://github.com/pybites/100DaysOfCode/blob/master/084/ghstats.py"""
    repos = []
    for repo in user.get_repos():
        if repo.fork:
            continue

        repos.append(Repo(name=repo.name,
                          stars=repo.stargazers_count,
                          forks=repo.forks_count))

    return sorted(repos, key=lambda x: x.stars, reverse=True)[:n]




if __name__ == '__main__':
    main()