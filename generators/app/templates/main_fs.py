from gradefast.test import GFTest
from gradefast.utils import Downloader
from gradefast.evaluate import Evaluate
from gradefast.aggregate import Aggregate
from gradefast.result import ResultGroup
from gradefast.submission import SubmissionGroup, Submission, LoadSubmissions

from test import <%= camelCaseTestName %>

# change this url of the task page to the one shown on
task_url = 'http://portal.e-yantra.org/admin/grade/<%= taskName %>'
task_name = <%= taskName %>
theme_name = <%= themeName %>

# list of items to download
types = ['txt', 'zip', 'py', 'bag']

# the cookie is obtained from web portal
cookie = '... ADD YOUR COOKIE HERE ...'

# since you selected from fs, this block is comment
# submission_group = LoadSubmissions.from_url(task_url, cookie, task_name, theme_name,
# types=types).get_submissions()

# to download the files or path of downloaded files
storage_location = './downloads'

# enable this option if you have already downloaded the submissions
submission_group = LoadSubmissions.from_fs(storage_location, task_name,
theme_name).get_submissions()

# configuration for download
downloader = Downloader(cookie, types=types, storage_location=storage_location,
extract=True)

# start the download
submission_group, download_directory = downloader.download(submission_group) # path to downloaded folder

test = <%= camelCaseTestName %>()
evaluate = Evaluate(test)
# # run evaluate
result_group, exception = evaluate(submission_group)
