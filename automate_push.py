from git import Repo, GitCommandError

wsdir="/auto/tftp-blr-users4/vsampree/python_scripts"
bugid="bugid"
branchlist="branch"
commitmsg="commit msg"




repo = Repo(wsdir)
branch=bugid+"."+branchlist


try:
	stat, ret, err = repo.git.execute(('git branch %s' %(branch)).split(), with_extended_output=True)
except GitCommandError as ex:
        print(ex)
	#raise RuntimeError("git branch failed\n%s"%(str(ex)))

print("git branch passed: ")

try:
	stat, ret, err = repo.git.execute(('git checkout %s' %(branch)).split(), with_extended_output=True)
except GitCommandError as ex:
	raise RuntimeError("git checkout failed\n%s"%(str(ex)))

print("git checkout passed: ",ret)


try:
	stat, ret, err = repo.git.execute(('git add *').split(), with_extended_output=True)
except GitCommandError as ex:
	raise RuntimeError("git add failed\n%s"%(str(ex)))

print("git add passed: ",ret)

commitmsg=commitmsg.replace(" ","_")
try:
    stat, ret, err = repo.git.execute(('git commit -m \'commit_test2\'').split(), with_extended_output=True)
except GitCommandError as ex:
	raise RuntimeError("git commit failed\n%s"%(str(ex)))

print("git commit passed: ",ret)

try:
	stat,ret,err = repo.git.execute(('git push origin %s' %(branch)).split(), with_extended_output=True)
except GitCommandError as ex:
	raise RuntimeError("git push failed\n%s"%(str(ex)))

#output=foo.stderr.split()
print("git push passed: ",err)
#print("stat: ",stat)
