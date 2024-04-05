# Fledger
Fledging is the stage in a flying animal's life between hatching or birth and becoming capable of flight.

Fledger is a Python Framework that simplifies software engineering and development under standards. It can be used by internal and opensource teams to help identify gaps, bring new team members up to speed, and aid in evidence collection. For people in training such as Software Engineers, Product Managers, or other positions it can be used to create a training reference guide using an OpenSource project as an example.

## High Level Areas Fledgler covers.
- Quality (Standards, Testing, Performance)
- Documentation (READMEs, Legal, Guides, CheatSheets)
- Release Notes
- Security

### Who is this for?
Status (Verified) is confirmed by multiple people added to the repo. Quotes TBD. (FEEDBACK TBD) is in the pipeline.


- Engineering Job Seekers
  - Use best in class standards and opensource code bases to learn
  - Have actual records of your work
  - Have a structured guide to help you 
- Technical Startup founders, Engineering Managers trying to improve their hiring process.
  - Building Rubrics, Scores, and allignment can take weeks. - (Verified)
  - Reduce Scoring and Feedback time - (Verified)
- Opensource founders
  - Use it to get started correctly just getting started can take 2+ weeks to it right. - (Verified)
  - Use it to assess and get the help you need on your project (FEEDBACK TBD)
- Security & Compliance Teams
  - Use it to reduce friction and drive adoption for training requirements, interviews, and other relevant areas. (FEEDBACK TBD)


### Getting Started

```sh
pip install fledger
```

Checkout a project in the language your interested in prepping for. Try to find a [OpenSSF](https://www.bestpractices.dev/en/projects) project that matches the domain experience or stack of the company. Create a clone of the project to checkout from.
```sh
git checkout xxx project
```

Do an assessment scan of the project to see if its up to [OSS Standards](https://www.bestpractices.dev/en/criteria/0?details=true&rationale=true).
```sh
fledger build-project-assesment openSSFBestPractices
```

This will generate an output in the /assements folder with the following files.

Create a user skills and project matrix using the standard.

Do an assessment scan of the project to see if its up to [OSS Standards](https://www.bestpractices.dev/en/criteria/0?details=true&rationale=true).
```sh
fledger build-skill-assesment openSSFBestPractices
```

After checking the matrix in folder (x) write some code and commit and run command.
```sh
git add .
git commit -m "Privacy Standards update"
fledger update-skill-assement
```

After a general commit to check the project status simply run.
```sh
fledger update-project-assement
```


### Help and additional Commands

```sh
fledger # or --help should respond with the optional fledger commands.
```