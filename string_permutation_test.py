from string_permutation import Permutations

class TestPermutation:
    def test_permutation(self):
        permutations = Permutations()
        assert permutations.is_permutation(None, 'foo') == False
        assert permutations.is_permutation('', 'foo') == False
        assert permutations.is_permutation('Nib', 'bin') == False
        assert permutations.is_permutation('act', 'cat') == True
        assert permutations.is_permutation('a ct', 'ca t') == True
        assert permutations.is_permutation('dog', 'doggo') == False

    