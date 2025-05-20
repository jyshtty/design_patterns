## Observer Design Pattern

The Pub/Sub (Publish/Subscribe) pattern is a classic example of the Observer design pattern.

**Explanation:**

In the Observer pattern, there is a "subject" (sometimes called publisher) that maintains a list of observers (subscribers).  
When the subject's state changes, it notifies all registered observers.  
The observers can subscribe (register) or unsubscribe (unregister) to receive updates.  
Your file `observer.py` defines an abstract `Observer` class and methods to register/unregister with a `Subject`, which fits the Observer pattern exactly.

**In summary:**  
**Pub/Sub is an implementation of the Observer design pattern.**
# design_patterns


![alt text](image.png)