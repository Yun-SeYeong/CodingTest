#!/bin/sh

# Credits: http://stackoverflow.com/a/750191

git filter-branch -f --env-filter "
    GIT_AUTHOR_NAME='Yun-SeYeong'
    GIT_AUTHOR_EMAIL='dbstpdud09@naver.com'
    GIT_COMMITTER_NAME='Yun-SeYeong'
    GIT_COMMITTER_EMAIL='dbstpdud09@naver.com'
  " HEAD

