Thank you for being a Tester!

Download the repository. Command examples can be found in the main command folder of the cli.


# Legacy Steps

Install Fledger

```sh
pip install fledger
```

Checkout a project in the language you're interested in prepping for. Try to find a [OpenSSF](https://www.bestpractices.dev/en/projects) project that matches the domain experience or stack of the company. Create a clone of the project to checkout from.
```sh
git checkout xxx project
```

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