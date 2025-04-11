import unittest
from unittest.mock import patch, MagicMock
import os
import main  # Assuming your main script is named main.py
import argparse
import sys

class TestMain(unittest.TestCase):

    @patch('os.getenv')
    def test_setup_gemini_api_success(self, mock_getenv):
        """Test that setup_gemini_api configures genai when the API key is present."""
        mock_getenv.return_value = "test_api_key"
        try:
            main.setup_gemini_api()
        except ValueError:
            self.fail("setup_gemini_api() raised ValueError unexpectedly!")

    @patch('os.getenv')
    def test_setup_gemini_api_missing_key(self, mock_getenv):
        """Test that setup_gemini_api raises ValueError when the API key is missing."""
        mock_getenv.return_value = None
        with self.assertRaises(ValueError):
            main.setup_gemini_api()

    @patch('main.genai.GenerativeModel')
    def test_generate_content(self, mock_generative_model):
        """Test that generate_content calls the Gemini API and prints the response."""
        mock_model = MagicMock()
        mock_chat = MagicMock()
        mock_response = MagicMock()
        mock_response.text = "Test response"
        mock_chat.send_message.return_value = mock_response
        mock_model.start_chat.return_value = mock_chat
        mock_generative_model.return_value = mock_model

        with patch('builtins.print') as mock_print:
            main.model = mock_model
            main.chat = mock_chat
            main.generate_content("Test prompt")

            mock_chat.send_message.assert_called_once_with("Test prompt")
            # Check if print was called for each character in the response text.
            expected_calls = [unittest.mock.call(char, end='', flush=True) for char in "Test response"]
            self.assertEqual(mock_print.call_args_list, expected_calls)

    @patch('sys.exit', side_effect=SystemExit)
    @patch('builtins.input', side_effect=['exit()'])
    @patch('argparse.ArgumentParser.parse_args')
    @patch('main.genai.GenerativeModel')
    def test_main_exit(self, mock_generative_model, mock_parse_args, mock_input, mock_exit):
        """Test that main exits when the user types 'exit()'."""
        mock_parse_args.return_value = argparse.Namespace(model_name='test_model')

        # Patch generate_content to bypass any actual API calls.
        with patch('main.generate_content'):
            with self.assertRaises(SystemExit):
                main.main()
        # Ensure sys.exit was called.
        mock_exit.assert_called_once()

    @patch('sys.exit', side_effect=SystemExit)
    @patch('builtins.input', side_effect=['exit()'])
    def test_accepts_model_argument(self, mock_input, mock_exit):
        """Test that main.py accepts a model argument from the CLI and initializes correctly."""
        custom_model = "custom-model"
        # Patch sys.argv to simulate command line argument
        test_argv = ['main.py', custom_model]
        with patch('sys.argv', test_argv):
            with patch('main.genai.GenerativeModel') as mock_generative_model:
                # Patch generate_content to avoid executing the actual loop.
                with patch('main.generate_content'):
                    with self.assertRaises(SystemExit):
                        main.main()
                # Ensure our custom model argument was used to initialize the model.
                mock_generative_model.assert_called_once_with(custom_model)
                mock_exit.assert_called_once()

if __name__ == '__main__':
    unittest.main()