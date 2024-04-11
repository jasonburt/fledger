# Fledger
Fledging is the stage in a flying animal's life between hatching or birth and becoming capable of flight.

Fledger is a Python Framework that simplifies software engineering and development under standards. It can be used by internal and opensource teams to help identify gaps, bring new team members up to speed, and aid in evidence collection. For people in training such as Software Engineers, Product Managers, or other positions it can be used to create a training reference guide using an OpenSource project as an example.



## High Level Areas Fledgler covers.
- Quality (Standards, Testing, Performance)
- Documentation (READMEs, Legal, Guides, CheatSheets)
- Release Notes
- Security

### Who is this for?

- **Engineering Job Seekers**
  - "Study and Build best practices using internal or Opensource projects instead of Leet Code."
  - Use best in class standards and opensource code bases to learn
  - Have actual records of your work
  - Have a structured guide to help you
- **Technical Startup founders**, **Engineering Managers** trying to improve their hiring process.
  - Building Rubrics, Scores, and allignment can take weeks. - (Verified)
  - Reduce Scoring and Feedback time - (Verified)
- **Opensource founders**
  - Use it to get started correctly just getting started can take 2+ weeks to it right. - (Verified)
  - Use it to assess and get the help you need on your project (FEEDBACK TBD)
- **Security & Compliance Teams**
  - Use it to reduce friction and drive adoption for training requirements, interviews, and other relevant areas. (FEEDBACK TBD)


### Getting Started

```sh
pip install fledger
```

Checkout a project in the language your interested in prepping for. Try to find a [OpenSSF](https://www.bestpractices.dev/en/projects) project that matches the domain experience or stack of the company. Create a clone of the project to checkout from.
```sh
git checkout xxx project
```

### Project Assessment
Do an assessment scan of the project to see if its up to [OSS Standards](https://www.bestpractices.dev/en/criteria/0?details=true&rationale=true).
```sh
fledger build-project-assesment openSSFBestPractices
```

This will generate an output in the **/assessments/project/overview_project.md** folder.

```sh
fledger search 'README*' --search-type=file --save=user
```
### User Assessment
Creates a user skills and project matrix using the standard entered
Do an assessment scan of the project to see if its up to [OSS Standards](https://www.bestpractices.dev/en/criteria/0?details=true&rationale=true).
```sh
fledger build-skill-assesment openSSFBestPractices
```

This generates an assessment file in **/assessments/users/overview_skills_and_project.md**.
Next create a **Record**
```sh
fledger search 'README*' --search-type=file --save=user
```
This creates a record with a code example that matches the pattern in the code. **/assessments/users/evidence.json**

Update your user assessment with records by running the update command.
```sh
fledger update-skill-assessment user
```

This updates the Skills and Project matrix.

**Backlog Functionality**
Optionally, you can fix some code and save the commit.
```sh
git add .
git commit -m "Privacy Standards update"
fledger update-skill-assement user
```

### Help and additional Commands

```sh
fledger # Running base command or --help should respond with the optional fledger commands.
```

## License

Fledger is licensed under the [Apache-2.0](https://opensource.org/licenses/APACHE-2.0) license.

## Contributing

Contributions are welcome! This community and project would not be what it is without the [contributors](https://github.com/jasonburt/fledger/graphs/contributors). All contributions, from bug reports to new features, are welcome and encouraged. Please view the [contribution guidelines](/CONTRIBUTING.md) before getting started.
