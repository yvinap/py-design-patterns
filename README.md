# Design Patterns - Bridge vs Adapter
This repository demonstrates the usage of Bridge and Adapter Design Patterns within a surveillance system module that manages device objects. The module supports creating, updating, deleting, and listing device objects. For explaining the design patterns, I have used the logging component to explain importance of bridge and adapter design pattern. 
You will observe that there are three separate branches apart from main branch

- scattered-logs: this branch shows, how the code for logging will look like without any design pattern
- bridge-design-pattern: this branch has the code after implementing the bridge design pattern
- adapter-design-pattern: this branch has the code after implementing the adapter design pattern.

You can toggle between each branch on GitHub to see how the code differs in each branch. 
Foe this exercise we will observe following part of code on each branch
- how the classes are implemented inside logger_system folder for each design pattern
- initialization of logger inside ApplicationFacade.__init__() 
- changes made to delete_device() function in device_manager class

The application is fully executable on each branch.  To run the application, clone the repository and execute it from the root directory. This will start the API server. APIs can be accessed via the command line using the curl command or through Postman.  
Here is sample GET request: 
http://127.0.0.1:5000/api/devices

## Before Bridge Pattern
Initial commit of the application had several log messages scattered throughout. The purpose of the log statements was to see how the message flow when the application us running.  The logging was mostly using the print statements scattered throughout the application. 
Here is the [link](https://github.com/yvinap/py-design-patterns/blob/scatterred-logs/src/domain/device_manager.py) for git branch to show how the code looked like for the initial commit of the module. 

## 1. Bridge Pattern

### Problem it solves:
- Separates abstraction from its implementation so that both can vary independently 
- Bridge pattern is applied during initial design, anticipating the need for different abstractions and implementations

### Use Case: 
Introduction of Logging Component in application for structured logging 
- Design a new logging system that separates the logging abstraction from its implementation. 
- Create two separate abstractions, one will used for application logging another will be used for user change logging (changes made to domain) 
- Create two separate implementations, one will support logging to console other will support logging to File.
- Demonstrated that abstraction and implementations can be changed independently

### Justification to use bridge pattern:
- Logging often requires different output methods. Thus in the future there may be need for new output method such as write to a database system.Bridge pattern supports this flexibility for future implementations. Also, it allow flexibility to modify logging abstractions so that, application logger and user changes logger have their own implementation. Observe [here](https://github.com/yvinap/py-design-patterns/blob/bridge-design-pattern/src/logger_system/loggers/user_change_logger.py) how the way  user_change_log.py have implemented delete_record_log_audit() independently of implementation  

### Without Bridge Pattern:
As you can see, without the bridge pattern there was no flexibility to modify the logging functionality. If any change was needed, it needs to be done in every file of the application where logging statements were implemented.

## 2. Adapter Pattern:
### Problem it solves:
- Converts the interface of a class into another interface that clients expect. Allows the classes work together that couldn't otherwise because of incompatible interfaces.
- Adapter pattern is applied after the application design is already in place. It helps to adapt to the new interface which is incompatible with current interface.  

### Use case:
- We had an existing logging system already designed. 
- Later a new **external CloudLogService logger** needed to be supported by application. CloudLogService had an incompatible interface and since it’s an external library we have no control over its source code. (Note that fot this exercise, we are showing its external nature by putting the ext_cloud_log_service.py inside the external_lib folder. Even though you can see the code of this class, assume that it was a Blackbox for us)
- We should not require changing the existing design of our application to support the new incompatible logger. 
- Also, we should achieve it with minimal changes to the existing code

### Justification to use Adapter Pattern:
- To avoid changes to our application design, we need to preserve the existing Bridge Pattern (Open/Close principle)
- To support the new CloudLogService library we created **CloudLogAdapter** which inherits LoggerImplementation and encapsulates CloudLogService 
- This way we maintained the separate of concerns new incompatible logger support from existing design for logging system

### Without Adapter Pattern:
- If we had to support CloudLogService without Adapter Pattern, then we would need to modify the Bridge Pattern to accommodate new implementation
- If the implantation interface would have to be changed the application code had to be modified all over where the logger implementation was used. This would have violated the Open/Close principle
