from gradefast.test import TestType, GFTest

class <%= camelCaseTestName %>(GFTest):
    def __init__(self):
        super().__init__(TestType.FILE, 'text')

    def __call__(self, file_path, submission):
        # GFTest requires this method to be implemented
        # we will write evaluation logic here
        
        # expected output
        # each of the correct words fetch different marks
        expected_words = ['Musical', 'Tenzin', 'Random', 'Calcifer', 'Shirucafe']

        # notice the file_path and submission parameters
        # these parameters are inserted in this test automatically
        # by another gradefast module called Evaluate
        result_dict = {}
        with open(file_path, 'r') as text_file:
            submission_words = text_file.readlines()
            # trim spaces and newlines
            submission_words = list(map(lambda submission_word: submission_word.strip(), submission_words))
            count_correct_words = 0
            for word in expected_words:
                if word in submission_words:
                    # for each of the word that is present add that word
                    # in dictionary and set value to 1 
                    result_dict[word] = 1
                    count_correct_words += 1
            return result_dict, 'You guessed {} words properly'.format(count_correct_words), None
