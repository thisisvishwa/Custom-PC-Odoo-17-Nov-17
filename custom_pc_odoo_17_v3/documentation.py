```python
class Documentation:
    def __init__(self):
        self.developer_docs = self._generate_developer_docs()
        self.user_help_docs = self._generate_user_help_docs()

    def _generate_developer_docs(self):
        return {
            "code_structure": "Detailed guide on the code structure can be found in the README.md file in the root directory.",
            "module_architecture": "The module architecture is detailed in the ARCHITECTURE.md file in the root directory.",
            "custom_APIs": "Documentation for custom APIs can be found in the APIs.md file in the root directory."
        }

    def _generate_user_help_docs(self):
        return {
            "site_navigation_guide": "A comprehensive guide on how to navigate the site can be found in the HELP.md file in the root directory.",
            "FAQ_section": "Frequently asked questions are addressed in the FAQ.md file in the root directory.",
            "troubleshooting_tips": "For troubleshooting tips, please refer to the TROUBLESHOOTING.md file in the root directory."
        }

    def get_developer_docs(self):
        return self.developer_docs

    def get_user_help_docs(self):
        return self.user_help_docs
```