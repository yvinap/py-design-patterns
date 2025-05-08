# Design Patterns - Bridge vs Adapter
This repository demonstrates the usage of Bridge and Adapter Design Patterns within a surveillance system module that manages device objects. The module supports creating, updating, deleting, and listing device objects. To run the application, clone the repository and execute it from the root directory. This will start the API server. APIs can be accessed via the command line using the curl command or through Postman. 
Here is sample GET request: 
http://127.0.0.1:5000/api/devices

## 1. Bridge Pattern

### Problem it solves:
- Separates and abstraction from its implementation so that both can vary independentlyt 
- Bridge pattern is applied during initial design, anticipating the need for different implementations

### Use Case: 
Design a Logging Component such that 
- Design a new logging system that separates the logging abstraction from its implementation. 
- Create two separate implememtations Console Logger and File Logger.
- There should be flexibility to change the Logger implementation without any impact on application components that uses logging
- Anticipate a need for different logger type in future. Consider that File logger is a future implementation that you would support

### Justification to use bridge pattern:
- Logging often requires different output methods. Thus in the future there may be need for new output method such as write to a database system.Bridge pattern supports this flexibility for future implementations  

### Without Bridge Pattern:
Initial commit of the application had several log messages scatterred throughout. The initial purpose of the log statements was to see the message flow when the application us running.  The loggin was mostly using the print statements scattered throughout the application. 
Here is the [link](https://github.com/yvinap/py-design-patterns/pull/1/commits/80b9930ce509ae3b05d5e5d7f11d68ed5c6d71a7) for git repository commit to show how the code looked like for the initial commit of the module. 

As you can see, without the bridge pattern there was no flexibility to modify the logging functionality. If any change was needed, it need to be done in every file of the application where logging statements were implemented.

## 2. Adapter Pattern:
### Problem it solves:
- Convert the interface of a class into another interface, clients expect. Lets classes work together that couldn't otherwise because of incompatible interfaces.
- Adapter pattern is applied after the interface were designed. 

### Use case:
- We had an existing ApplicationLogger interface. 
- Later a new CloudLogService needed to be supported by application. CloudLogService had an incompatible interface
- We should not change the existing design of our application to support the new incompatible logger

### Justification to use Adapter Pattern:
- In order to avoid changed to our application design, we need to preserve the existing Bridge Pattern
- Thus to support the new CloudLogService we created CloudLogAdapter which inherits LoggerImplementation
- This way we maintained the separate of concerns (logging abstraction vs implementation)

### Without Adapter Pattern:
- If we had to support CloudLogService without Adapter Pattern, then we would need to modify the Bridge Pattern to accomodate new implementation
- If the implemtation interface would have to be changed the application code had to be modifer all over where the logger implementation was used. This would have voilated the Open/Close principle
 
