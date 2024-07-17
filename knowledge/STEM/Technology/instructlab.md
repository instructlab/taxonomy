# InstructLab

Welcome to the InstructLab CLI
InstructLab 🐶 uses a novel synthetic data-based alignment tuning method for Large Language Models (LLMs.) The "lab" in InstructLab 🐶 stands for Large-Scale Alignment for ChatBots [1].

[1] Shivchander Sudalairaj*, Abhishek Bhandwaldar*, Aldo Pareja*, Kai Xu, David D. Cox, Akash Srivastava*. "LAB: Large-Scale Alignment for ChatBots", arXiv preprint arXiv: 2403.01081, 2024. (* denotes equal contributions)

🎺 What's new
InstructLab release 0.17.0 on June 14, 2024 contains updates to the ilab CLI design. The ilab commands now fall into groups for an easier workflow and understanding of the commands. For more information, see the InstructLab CLI reference To view all the available flags for each command group, use the --help tag after the command. The original commands are still in effect, but will be deprecated in release 0.19.0 on July 11, 2024.

❓ What is ilab
ilab is a Command-Line Interface (CLI) tool that allows you to perform the following actions:

Download a pre-trained Large Language Model (LLM).
Chat with the LLM.
To add new knowledge and skills to the pre-trained LLM, add information to the companion taxonomy repository.

After you have added knowledge and skills to the taxonomy, you can perform the following actions:

Use ilab to generate new synthetic training data based on the changes in your local taxonomy repository.
Re-train the LLM with the new training data.
Chat with the re-trained LLM to see the results.
