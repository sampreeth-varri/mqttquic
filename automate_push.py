from git import Repo, GitCommandError



git_root="/auto/tftp-blr-users4/vsampree/python_scripts"
repo = Repo(git_root)

try:
	stat, ret, err = repo.git.execute(('git branch branch1').split(), with_extended_output=True)
except GitCommandError as ex:
	raise RuntimeError("git branch failed\n%s"%(str(ex)))

print("git branch passed: ",err)


try:
	stat, ret, err = repo.git.execute(('git add *').split(), with_extended_output=True)
except GitCommandError as ex:
	raise RuntimeError("git add failed\n%s"%(str(ex)))

print("git add passed: ",ret)

try:
    stat, ret, err = repo.git.execute(('git commit -m \"commit_test2\"').split(), with_extended_output=True)
except GitCommandError as ex:
	raise RuntimeError("git commit failed\n%s"%(str(ex)))

print("git commit passed: ",ret)

try:
	stat,ret,err = repo.git.execute(('git push origin brnach1').split(), with_extended_output=True)
except GitCommandError as ex:
	raise RuntimeError("git push failed\n%s"%(str(ex)))

#output=foo.stderr.split()
print("git push passed: ",err)
#print("stat: ",stat)
