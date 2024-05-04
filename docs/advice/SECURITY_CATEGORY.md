
# Fledger: Security Read Me

**Category Advisor:** Ben Ransford (Startup Founder, currently Security engineer at Stripe, not on behalf of Stripe)
## Why is Security important?

“Security” refers to the goal of making sure systems behave as designed, even when someone tries to make them behave otherwise. Errors in security can result in serious consequences for companies, including monetary loss or reputational damage. Getting security right means being able to understand how to make systems robust.

[https://www.schneier.com/blog/archives/2008/03/the_security_mi_1.html](https://www.schneier.com/blog/archives/2008/03/the_security_mi_1.html) is a short introduction to the “security mindset,” a way of thinking about systems through the eyes of an adversary that might want to make them misbehave.

**Understanding security** helps engineers build systems that behave as designed.

## How to use this Fledger to Practice for Security Interviews

Open-source software powers the world. Security issues can happen at a package, service, or system level. Here are some key areas that you can practice with an open source project. Search for a project here [link](https://github.com/trending?since=monthly), find something you like!

**Run this command** to generate the relative skill assessment to track
```sh
fledger build-skill-assesment SecurityCategory
```

|                        |                                                                 |                                                                                                                                                                                                                                                                                                                |
| ---------------------- | --------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Category**           | **Description**                                                 | **Steps**                                                                                                                                                                                                                                                                                                      |
| Package Analysis       | Understanding down stream package usage is important.           | Choose a project, pull one of the packages, which one would you map through the system? Whats the impact?                                                                                                                                                                                                      |
| Bug Check              |                                                                 | Choose a project, look at open bugs. Could any of the current bugs impact service or be exploited?                                                                                                                                                                                                             |
| System Analysis        | Take an existing system and explain how it works.               | Foundation for the threat model.                                                                                                                                                                                                                                                                               |
| Design A system        | Build a simple system that is reliable, boxes and drawings. : ) | Tell us what could go wrong!                                                                                                                                                                                                                                                                                   |
| Build a threat model   | Analyze a system to understand how it could be abused           | Explain the system<br><br>Explain your assumptions<br><br>Invert your assumptions<br><br>Repeat until you have walked through the main use cases<br><br>For each potential avenue of misuse, figure out what the attacker would gain from misusing it that way<br><br>Sort by value to an attacker, descending |
| Fix an insecure system | Given a set of risks, figure out how to address them            | Start with a threat model; consider misuse and then how to defend against that misuse<br><br>Consider how the system can still be useful even if it’s more defensive against attackers                                                                                                                         |

## Working with Security Teams.

Security teams have a shared mission to improve the quality of the product. Depending on the size of your organization Security teams might be internal or you might work with an external team doing a yearly audit. Security teams are normally one or two too many engineers. To set you up for success, prepping before you have a conversation is extremely helpful. Here are some tips for working with them. 

- “Security mindset” from above will give you a clue as to how they’re thinking.
- They’ll want to know if you’ve considered the security aspects of what you’re doing. Seed them with whatever you’ve already thought of.
- Be able to say what your system does and what it’s made of? Draw a block diagram of the moving parts
- To start thinking of security aspects, look at “security mindset”
- Did you read the README?
- How might your software be misused?
- Let’s build a basic threat model for your system
- How are you planning to test your system?
- What assumptions have you made about how your system will be used? What happens if you assume the user wants to make your system misbehave?
- Does your system have a notion of permissions? (Who can do what?)
- Does your system record a log of what it’s doing?

[https://sre.google/books/building-secure-reliable-systems/](https://sre.google/books/building-secure-reliable-systems/) is a good book about thinking through the design of a system with an eye toward security and robustness**