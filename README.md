# Fledger
Fledging is the stage in a flying animal's life between hatching or birth and becoming capable of flight.

Fledger is a Python Framework that simplifies software engineering and devlopment under standards. It can be used by internal and opensource teams to help identify gaps, bring new team members up to speed, and aid in evidence collection. For people in training such as Software Engineers, Product Managers, or other positions it can be used to create a training reference guide using an OpenSource project as an example.

## High Level Areas Fledgler covers.
- Quality (Standards, Testing, Performance)
- Documentation (READMEs, Legal, Guides, CheatSheets)
- Release Notes
- Security

### Getting Started

```sh
pip install fledger
```

Checkout a project in the language your interested in prepping for. Try to find a [OpenSSF](https://www.bestpractices.dev/en/projects) project that matches the domain experience or stack of the company. Create a clone of the project to checkout from.
```sh
git checkout xxx project
```

Do an assesment scan of the project to see if its up to [OSS Standards](https://www.bestpractices.dev/en/criteria/0?details=true&rationale=true).
```sh
fletcher build-standards openSSFBestPractices
```

This will generate an output in the /standards folder with the following files.
- Overview Gap Analysis

After checking the matrx in folder (x) write some code and commit and run command.
```sh
git add .
git commit -m "Privacy Standards update"
fletcher update-standards
```




### Help and additional Commands

```sh
fledger # or --help should respond with the optional fledger commands.
```
