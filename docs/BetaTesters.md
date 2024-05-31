Thank you for being a Tester!

# Friction Log
Before you start testing, please take notes. In the industry these are commonly called Friction logs. They don't have to be deep. Just what a sentance on what you testing followed by key steps. If something is great, or not great please make a note. We can't go deep on everything, so if you are an approved Beta Tester we would love to read the notes and you can share them directly and/or attach them to a bug.

# Primary Testing : Using the Fledger Repository
The default is to test new features from the main codebase or a branch that someone is working on.
- Download the repository.
- In the repository create a sym link or alias so you can call the command, to avoid conflicting with fledger, we recommend using the name bfledger.
```alias bfledger='python cli/main.py'```
- navigate to a different directory or open a new terminal
- ```run bfledger --help ```

Command examples can be found in the main command folder of the cli.

# Running Tests
Tests are in src/tests section. We start with snapshot tests for new commands and each optional input of the command, Snapshot testing is a type of “output comparison” where we test the command output and record output.

- Navigate to root of the project
- python -m pytest
- This will run through the sanpshot tests for each command.

# Commands
### Project Assessment
Do an assessment scan of the project to see if its up to [OSS Standards](https://www.bestpractices.dev/en/criteria/0?details=true&rationale=true). You can copy the example file from this project.
```sh
fledger build-project-assesment openSSFBestPractices
```

This will generate an output in the **/assessments/project/overview_project.md** folder.

```sh
fledger search 'README*' --search-type=file --save=project --category=Basics --subcategory=Documentation
```
### User Assessment
Creates a user skills and project matrix using the standard entered
Do an assessment scan of the project to see if its up to [OSS Standards](https://www.bestpractices.dev/en/criteria/0?details=true&rationale=true).
```sh
fledger build-skill-assesment openSSF
```

This generates an assessment file in **/assessments/users/overview_skills_and_project.md**.
Next create a **Record**
```sh
fledger search 'README*' --search-type=file --save=user --category=Basics --subcategory=Documentation
```
This creates a record with a code example that matches the pattern in the code. **/assessments/users/evidence.json**

Update your user assessment with records by running the update command.
```sh
fledger update-skill-assessment user
```


```

### Help and additional Commands

```sh
fledger # Running base command or --help should respond with the optional fledger commands.
```
