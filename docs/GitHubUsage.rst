############
GitHub Usage
############

Introduction
************
This guide takes you through various commands / steps required when working
with GitHub.

Git (CLI)
*********
Setting up local repo via fork
==============================
1. Fork this repository.
2. ``cd`` into the directory where you want to clone repository into.
3. ``git clone <forked_repository_url>`` to clone repository.
4. ``cd`` into the cloned repository.
5. Set *upstream* to track original repository by:
   
   * ``git remote add upstream <original_repository_url>``.
   * ``git branch --set-upstream-to=upstream/master master``.
6. You're ready to work with your local repository.

Adding file(s) to be committed
==============================
1. ``git add <file>`` to add file(s).
2. ``git restore --staged <file>`` to remove staged file(s).
3. ``git rm <file>`` to remove file(s). (usually during conflict resolution)

Committing changes
==================
1. ``git commit -m "<message>"`` to commit change(s).
2. Find commit's hash by ``git log``, and searching through various commits.
3. ``git revert <commit_hash>`` to revert commit.

Pushing changes to remote
=========================
1. ``git status`` to check if everything is according to you.
2. Add file(s) and commit if needed.
3. Push changes to remote using:
   
   * ``git push -u <remote_name> <branch>`` if this is first time you're
      pushing changes and / or if you want to set the provided *remote* and
      *branch* as default, where *remote name* is generally *origin*.
   * ``git push <remote_name> <branch>`` to push changes to specified *remote*
      and *branch*.
   * ``git push`` to push to currently set *remote* and *branch*.

Rebasing for merge conflict
===========================
1. ``git fetch upstream`` to fetch updated file(s) from upstream.
2. ``git rebase upstream/master`` to apply fetched update(s) and then our
   commits released later.
3. Update or change file(s) to resolve conflicts if any.
4. ``git rebase --continue`` to continue with rebase.
5. ``git rebase --abort`` to abort rebase process if you don't want to continue
   or if something goes wrong.
6. Continue working.

Combining multiple commits into one
===================================
1. ``git log`` to get *hash value* of oldest commit's parent.
2. ``git rebase -i <hash_value>`` to run interactive rebase.
3. Work on file(s) and commit changes.
4. Push changes with:
   
   * ``git push``.
   * ``git push -f``, if any error occurs in ``git push``.

Switch to another branch
========================
1. ``git branch --list`` to list all available branches to switch to.
2. Switch to another branch by:
   
   * ``git switch <branch>``.
   * ``git checkout <branch>``.
   * Use ``cd <path>`` only if you added separate **worktree** for a branch.

Creating new branch
===================
1. Make sure current branch tree is clean and no other push or commit is
   pending.
2. Switch to branch from where you want to make a new branch.
3. ``git checkout -b <branch>`` to create new branch and immediately switch
   to it.
4. Push *new branch* to remote / upstream by:
   
   * ``git push origin <new_branch>``.
   * ``git push -u origin <new_branch>`` to set *new branch* to upstream.

Deleting a branch
=================
1. Switch to a different branch, other than the one which you want to delete.
2. Delete branch locally by:
   
   * ``git branch -d <branch_to_delete>``.
   * ``git branch -D <branch_to_delete>`` to force delete branch.
3. ``git push origin --delete <branch_to_delete>`` to delete branch from
   remote as well.

Updating feature branch with latest commits to main branch
==========================================================
1. Switch to feature branch.
2. ``git merge origin/main``.
3. ``git status`` to check for conflicts.
4. Resolve all conflicts.
5. ``git commit -m "<message>"`` if changes are made.
6. ``git push`` to push changes to remote as well.

Merge feature branch to main branch
===================================
1. Switch to feature branch.
2. Update feature branch with latest commits of main branch.
3. ``git push origin <feature_branch>`` to update remote *feature branch*.
4. Switch to *main* branch.
5. ``git pull origin main`` to update local *main* branch with remote *main*
   branch.
6. ``git merge <feature_branch>`` to merge *feature* branch to *main* branch.
7. Remove conflicts, if any, and commit changes.
8. ``git push origin main`` to push changes to remote.
9. Delete *feature branch* if not required anymore.

Parallelly working on multiple branches
=======================================
1. ``mkdir <directory_name>`` to the location where you want your selected
   branch to be at.
2. ``cd`` to local git repository.
3. ``git worktree add <path> <branch>``, where path is pointing to the
   directory which you just created in *step 1*. Repeat all steps for all such
   branches whom you want to work on.
4. ``cd <path>`` to directory instead of switching branch otherways.
5. New dedicated directory based branch is ready to be used without any fear
   of changes getting lost while switching branches. (this does not create any
   new branch)
6. ``git worktree remove <path>`` to remove separate worktree for *branch*
   associated with the *path*. (provided while creating)

GitHub website
**************

GitHub CLI
**********

GitHub GUI
**********
