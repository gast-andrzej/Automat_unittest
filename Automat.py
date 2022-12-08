class AutomatUnittests:

    def _opener_user(self):
        _name_filex = input("Your name for testing file ")
        opener = open(f"{_name_filex}.py", "a")
        opener.write("import unittest\n"
                     "\n"
                     "\n"
                     "\n"
                     "class TestClass(unittest.TestCase):")
        return opener

    def _opener_automat(self):
        opener = open(f"Test.py", "a")
        opener.write("import unittest\n"
                     "\n"
                     "\n"
                     "\n"
                     "class TestClass(unittest.TestCase):")
        return opener

    def funcinit(self=None):
        opener = None
        print("Welcome in unit testing automat. Remember, this automat works as an object\n"
              "and append testing file.\n"
              "\n"
              "\n"
              "")
        name_file = input("You want creating name for your testing file or you want default? [Y/N] ")
        match name_file:
            case "Y":
                opener = AutomatUnittests._opener_user(self)
            case "y":
                opener = AutomatUnittests._opener_user(self)
            case "N":
                opener = AutomatUnittests._opener_automat(self)
            case "n":
                opener = AutomatUnittests._opener_automat(self)
            case default:
                opener = AutomatUnittests._opener_automat(self)
        how_many_func_want_user = int(input("Welcome in unit testing automat. How many function unittest you want? "))

        type_test_func_user = int(input("How type tests you want? (only number)\n"
                                    "1.Assert Equal\n"
                                    "2.Assert True\n"
                                    "3.Assert False\n"
                                    "4.Assert Is\n"
                                    "5.Assert IsNone\n"
                                    "6.Assert In\n"
                                    "7.Assert Is Instance\n"))
        match type_test_func_user:
            case 1:
                for i in range(0,int(how_many_func_want_user)):
                    varex = input("Your function and variables to insert to function ")
                    varex_end = input("Your equal assert test ")
                    answer_if_fail = input("Here is You'r answer, if this test fail (easy, it's default str, don't worry)")
                    opener.write(f"\n    def test_{i}(self):\n"
                                 f"        self.assertEqual({varex}, {varex_end}, '{answer_if_fail}')\n"
                                 f"\n"
                                 f"")

                opener.close()
            case 2:
                for i in range(0, int(how_many_func_want_user)):
                    varex = input("Your function and variables to insert to function (boolean assert True, remember)")
                    answer_if_fail = input(
                        "Here is You'r answer, if this test fail (easy, it's default str, don't worry)")
                    opener.write(f"\n    def test_{i}(self):\n"
                                 f"        self.assertTrue({varex}, '{answer_if_fail}')\n"
                                 f"\n"
                                 f"")

                opener.close()
            case 3:
                for i in range(0, int(how_many_func_want_user)):
                    varex = input("Your function and variables to insert to function (boolean assert False, remember)")
                    answer_if_fail = input(
                        "Here is You'r answer, if this test fail (easy, it's default str, don't worry)")
                    opener.write(f"\n    def test_{i}(self):\n"
                                 f"        self.assertFalse({varex}, '{answer_if_fail}')\n"
                                 f"\n"
                                 f"")

                opener.close()
            case 4:
                for i in range(0, int(how_many_func_want_user)):
                    # positive and negative
                    # value in test, that same or not

                    indexer = input("you want p = is positive, or n = is negative testcase? ")
                    match indexer:
                        case "p":
                            varex = input("Your function and variables to insert to function ")
                            varex_end = input("Your equal assert test ")
                            answer_if_fail = input("Here is You'r answer, if this test fail (easy, it's default str, don't worry)")
                            opener.write(f"\n    def test_positive_{i}(self):\n"
                                         f"        first_val = {varex}\n"
                                         f"        sec_val = {varex_end}\n"
                                         f"        self.assertIs(first_val, sec_val, '{answer_if_fail}')\n"
                                         f"\n"
                                         f"")
                        case "P":
                            varex = input("Your function and variables to insert to function ")
                            varex_end = input("Your equal assert test ")
                            answer_if_fail = input(
                                "Here is You'r answer, if this test fail (easy, it's default str, don't worry)")
                            opener.write(f"\n    def test_positive_{i}(self):\n"
                                         f"        first_val = {varex}\n"
                                         f"        sec_val = {varex_end}\n"
                                         f"        self.assertIs(first_val, sec_val, '{answer_if_fail}')\n"
                                         f"\n"
                                         f"")
                        case "n":
                            varex = input("Your function and variables to insert to function ")
                            varex_end = input("Your equal assert test ")
                            answer_if_fail = input(
                                "Here is You'r answer, if this test fail (easy, it's default str, don't worry)")
                            opener.write(f"\n    def test_negative_{i}(self):\n"
                                         f"        first_val = {varex}\n"
                                         f"        sec_val = {varex_end}\n"
                                         f"        self.assertIs(first_val, sec_val, '{answer_if_fail}')\n"
                                         f"\n"
                                         f"")
                        case "N":
                            varex = input("Your function and variables to insert to function Is")
                            varex_end = input("Your equal assert test ")
                            answer_if_fail = input(
                                "Here is You'r answer, if this test fail (easy, it's default str, don't worry)")
                            opener.write(f"\n    def test_negative_{i}(self):\n"
                                         f"        first_val = {varex}\n"
                                         f"        sec_val = {varex_end}\n"
                                         f"        self.assertIs(first_val, sec_val, '{answer_if_fail}')\n"
                                         f"\n"
                                         f"")

            case 5:
                for i in range(0, int(how_many_func_want_user)):
                    varex = input("Your function and variables to insert to function IsNone")
                    answer_if_fail = input(
                        "Here is You'r answer, if this test fail (easy, it's default str, don't worry)")
                    opener.write(f"\n    def test_IsNone_{i}(self):\n"
                                 f"        first_val = {varex}\n"
                                 f"        self.assertIsNone({varex}, '{answer_if_fail}')\n"
                                 f"\n"
                                 f"")
            case 6:
                for i in range(0, int(how_many_func_want_user)):

                    indexer = input("you want p = is positive, or n = is negative testcase? ")
                    match indexer:
                        case "p":
                            varex = input("Your key in container ")
                            varex_end = input("Your container ")
                            answer_if_fail = input(
                                "Here is You'r answer, if this test fail (easy, it's default str, don't worry)")
                            opener.write(f"\n    def test_positive_{i}(self):\n"
                                         f"        key = {varex}\n"
                                         f"        container = {varex_end}\n"
                                         f"        self.assertIn(key, container, '{answer_if_fail}')\n"
                                         f"\n"
                                         f"")
                        case "P":
                            varex = input("Your key in container ")
                            varex_end = input("Your container ")
                            answer_if_fail = input(
                                "Here is You'r answer, if this test fail (easy, it's default str, don't worry)")
                            opener.write(f"\n    def test_positive_{i}(self):\n"
                                         f"        key = {varex}\n"
                                         f"        container = {varex_end}\n"
                                         f"        self.assertIn(key, container, '{answer_if_fail}')\n"
                                         f"\n"
                                         f"")
                        case "n":
                            varex = input("Your key in container ")
                            varex_end = input("Your container ")
                            answer_if_fail = input(
                                "Here is You'r answer, if this test fail (easy, it's default str, don't worry)")
                            opener.write(f"\n    def test_negative_{i}(self):\n"
                                         f"        key = {varex}\n"
                                         f"        container = {varex_end}\n"
                                         f"        self.assertIn(key, container, '{answer_if_fail}')\n"
                                         f"\n"
                                         f"")
                        case "N":
                            varex = input("Your key in container ")
                            varex_end = input("Your container ")
                            answer_if_fail = input(
                                "Here is You'r answer, if this test fail (easy, it's default str, don't worry)")
                            opener.write(f"\n    def test_negative_{i}(self):\n"
                                         f"        key = {varex}\n"
                                         f"        container = {varex_end}\n"
                                         f"        self.assertIn(key, container, '{answer_if_fail}')\n"
                                         f"\n"
                                         f"")
            case 7:
                for i in range(0, int(how_many_func_want_user)):

                    indexer = input("you want p = is positive, or n = is negative testcase? ")
                    match indexer:
                        case "p":
                            varex = input("Your object name ")
                            varex_end = input("instance class ")
                            answer_if_fail = input(
                                "Here is You'r answer, if this test fail (easy, it's default str, don't worry)")
                            opener.write(f"\n    def test_positive_{i}(self):\n"
                                         f"        obj = {varex}\n"
                                         f"        instance = {varex_end}\n"
                                         f"        self.assertIsInstance(obj, instance, '{answer_if_fail}')\n"
                                         f"\n"
                                         f"")
                        case "P":
                            varex = input("Your object name ")
                            varex_end = input("instance class ")
                            answer_if_fail = input(
                                "Here is You'r answer, if this test fail (easy, it's default str, don't worry)")
                            opener.write(f"\n    def test_positive_{i}(self):\n"
                                         f"        obj = {varex}\n"
                                         f"        instance = {varex_end}\n"
                                         f"        self.assertIsInstance(obj, instance, '{answer_if_fail}')\n"
                                         f"\n"
                                         f"")
                        case "n":
                            varex = input("Your object name ")
                            varex_end = input("instance class ")
                            answer_if_fail = input(
                                "Here is You'r answer, if this test fail (easy, it's default str, don't worry)")
                            opener.write(f"\n    def test_negative_{i}(self):\n"
                                         f"        obj = {varex}\n"
                                         f"        instance = {varex_end}\n"
                                         f"        self.assertIsInstance(obj, instance, '{answer_if_fail}')\n"
                                         f"\n"
                                         f"")
                        case "N":
                            varex = input("Your object name ")
                            varex_end = input("instance class ")
                            answer_if_fail = input(
                                "Here is You'r answer, if this test fail (easy, it's default str, don't worry)")
                            opener.write(f"\n    def test_negative_{i}(self):\n"
                                         f"        obj = {varex}\n"
                                         f"        instance = {varex_end}\n"
                                         f"        self.assertIsInstance(obj, instance, '{answer_if_fail}')\n"
                                         f"\n"
                                         f"")