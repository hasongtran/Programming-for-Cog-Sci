from assignment4 import *
import operator
import os

"""
Psych 138 Winter 2017
Assignment4 Test Code (Uses pytest module)
Travis Seymour, PhD
----------------------

If any of the function names below have red lines under them, that means
they are not yet defined in your code file. The red lines will automatically
go away as you define each function. You can still run this test, but
obviously tests for functions you have yet to create will fail as expected.

WARNING: Running while clicking within one of the test functions below may only run that one.
Click someone outside of a function below to run all the tests at once. There should be 26 total tests run.
"""


class TestModify:
    def setup_class(self):
        print('\n****Testing modify()\n')

    def test_normal_list(self):
        assert (modify(word_list=['Earth', 'day'], modifier='beautiful', the_text='Hello Earth, enjoy your day') ==
                'Hello beautiful Earth, enjoy your beautiful day')

    def test_normal_string(self):
        assert (modify(word_list='Earth,day', modifier='beautiful', the_text='Hello Earth, enjoy your day') ==
                'Hello beautiful Earth, enjoy your beautiful day')

    def test_bad_word_list(self):
        assert (modify(word_list=39493, modifier='beautiful', the_text='Hello Earth, enjoy your day') is None)

    def test_bad_modifier(self):
        assert (modify(word_list='Earth,day', modifier=34323, the_text='Hello Earth, enjoy your day') is None)

    def test_bad_text(self):
        assert (modify(word_list='Earth,day', modifier='beautiful', the_text=32343) is None)


class TestRandomFiles:
    def setup_class(self):
        print('\n****Testing random_files()\n')
        setup_folder(folder='randfiles')  # just to be thorough prior to testing
        random_files()  # should re-create randfiles anyway

    def test_files_exist(self):
        assert os.path.isdir('randfiles') == True
        files = os.listdir('randfiles')
        assert files == ['random1.txt', 'random2.txt', 'random3.txt', 'random4.txt', 'random5.txt', 'random6.txt',
                         'random7.txt', 'random8.txt', 'random9.txt']
        print('\tfound expected files in randfiles folder')

    def test_file_contents(self):
        spot_check = random.sample(range(1, 10), 2)
        for fnum in spot_check:
            fname = 'random'+str(fnum)+'.txt'
            with open(os.path.join('randfiles', fname), 'r') as infile:
                text = infile.read()
            assert text
            text_list = text.split(' ')
            assert len(text_list) == 10
            # list comprehension...we'll learn about these soon (not currently allowed)
            assert all([w in crawler for w in text_list])  # we'll also learn about how all() works
        print('\trandom files appear to each contain 10 randomly selected words from crawler')


class TestAllContent:
    def setup_class(self):
        print('\n****Testing all_content()\n')
        self.paragraph = all_content()

    def test_files_exist(self):
        assert os.path.isdir('randfiles') == True
        files = os.listdir('randfiles')
        assert files == ['random1.txt', 'random2.txt', 'random3.txt', 'random4.txt', 'random5.txt', 'random6.txt',
                         'random7.txt', 'random8.txt', 'random9.txt']
        print('\tfound expected files in randfiles folder')

    def test_output_is_str(self):
        assert type(self.paragraph) is str

    def test_output_punctuation(self):
        assert self.paragraph.replace(' ', '').replace('\n', '').isalpha()

    def test_output_lines(self):
        lines = self.paragraph.split('\n')
        assert len(lines) == 9

    def test_output_words(self):
        words = self.paragraph.replace('\n', ' ').split(' ')
        assert len(words) == 9 * 10


class TestLilStats:
    def setup_class(self):
        print('\n****Testing lil_stats()\n')

    def test_good_list1(self):
        assert lil_stats(values=[8, 6, 7, 5, 3, 0, 9]) == (5.428571428571429, 0, 9, 9, 7)

    def test_good_list2(self):
        assert lil_stats(values=[100, 23, 74, 99, 819, 23, 44, 14, 639]) == (203.88888888888889, 14, 819, 805, 9)

    def test_empty_list(self):
        assert lil_stats(values=[]) is None

    def test_non_list(self):
        assert lil_stats(values='8,6,7,5,3,0,9') is None


class TestLilStatsNT:
    def setup_class(self):
        print('\n****Testing lil_stats_nt()\n')
        self.result = lil_stats_nt(values=[8, 6, 7, 5, 3, 0, 9])

    def test_tuple(self):
        assert isinstance(self.result, tuple)

    def test_attributes(self):
        assert self.result.average == 5.428571428571429
        assert self.result.minimum == 0
        assert self.result.maximum == 9
        assert self.result.dispersion == 9
        assert self.result.N == 7


class TestBadKey:
    def setup_class(self):
        print('\n****Testing bad_key()\n')

    def test_good(self):
        assert not bad_key(dictionary={'one': 1, 'two': 2, 'three': 'tres', 'four': 'shi'})

    def test_bad(self):
        assert bad_key(dictionary={'one': 'bad', 'two': 2, 'three': 'tres', 'bad': 'shi'})


class TestBadValue:
    def setup_class(self):
        print('\n****Testing bad_value()\n')

    def test_good(self):
        assert not bad_value(dictionary={'one': 1, 'two': 2, 'three': 'tres', 'four': 'shi'})

    def test_bad(self):
        assert bad_value(dictionary={'one': 'bad', 'two': 2, 'three': 'tres', 'bad': 'shi'})


class TestWordCount:
    def setup_class(self):
        print('\n****Testing word_count()\n')

    def test_return(self):
        s = 'how much wood would a wood chuck chuck if a wood chuck could chuck wood'
        result = word_count(astring=s)
        assert type(result) is dict
        assert len(result.keys()) == 8

    def test_content(self):
        s = 'how much wood would a wood chuck chuck if a wood chuck could chuck wood'
        dict_result = word_count(astring=s)
        sorted_tuple_result = sorted(dict_result.items(), key=operator.itemgetter(0))
        assert sorted_tuple_result == \
               [('a', 2), ('chuck', 4), ('could', 1), ('how', 1), ('if', 1), ('much', 1), ('wood', 4), ('would', 1)]

    def test_one_word(self):
        assert word_count(astring='chuck') == {'chuck': 1}
        assert word_count(astring='') == {'': 1}

    def test_bad_input(self):
        assert word_count(astring=['how', 'much']) is None
        assert word_count(astring=1138) is None

