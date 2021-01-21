from git import Repo, GitCommandError



git_root="/auto/tftp-blr-users4/vsampree/python_scripts"
repo = Repo(git_root)
try:
	stat, ret, err = repo.git.execute(('git add *').split(), with_extended_output=True)
except GitCommandError as ex:
	raise RuntimeError("git add failed\n%s"%(str(ex)))

print("git add passed: ",ret)

try:
    stat, ret, err = repo.git.execute(('git commit -m \"commit\"').split(), with_extended_output=True)
except GitCommandError as ex:
	raise RuntimeError("git commit failed\n%s"%(str(ex)))

print("git commit passed: ",ret)

try:
	stat, ret, err = repo.git.execute(('git push origin master').split(), with_extended_output=True)
except GitCommandError as ex:
	raise RuntimeError("git push failed\n%s"%(str(ex)))

print("git push passed: ",ret)
