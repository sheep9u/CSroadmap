# Java

Java是美国sun公司（Stanford University Network）在1995年推出的一门计算机高级编程语言。2009年sun公司被Oracle公司收购。（Java之父：James Gosling）

它的设计目标是写一次，到处运行，这个目标一直延续至今

![Alt text](images/image-1.png)

以下是Java常见的用途：

1. **应用程序开发**：Java可以用于开发各种类型的应用程序，包括桌面应用程序、移动应用程序和Web应用程序。

2. **Android应用开发**：Java是Android平台上最主要的编程语言之一，用于开发移动应用程序。

3. **Web开发**：虽然Java不像Python或JavaScript那样常用于前端开发，但它在后端开发中非常流行。Java的一些流行框架如Spring和JavaServer Faces (JSF)用于构建Web应用程序。

4. **大数据和分布式计算**：Java在大数据领域非常重要，例如使用Apache Hadoop和Apache Spark进行分布式数据处理和分析。

5. **企业级应用开发**：Java广泛用于开发企业级应用程序，特别是大型企业系统和应用，它的稳定性和可维护性非常受欢迎。

6. **游戏开发**：虽然不如C++在游戏开发中流行，但Java仍然用于开发Android游戏和基于Java的游戏引擎。

7. **嵌入式系统**：Java可以用于嵌入式系统和物联网设备的开发，尤其是在需要跨平台兼容性的情况下。

8. **科学计算**：Java在科学和工程计算中也有应用，例如开发模拟和仿真软件。

9. **金融领域**：Java在金融行业中广泛使用，用于开发交易平台、风险管理系统和其他金融应用。

10. **教育**：Java通常作为教育和学术研究的编程语言，因为它的语法清晰，易于学习。

11. **桌面应用程序**：使用Java的图形界面库（如Swing和JavaFX），可以创建跨平台的桌面应用程序。

12. **安全性**：Java具有强大的安全性特性，用于开发安全性要求高的应用，如金融和医疗应用。

# JavaEE和Java的区别

JavaEE（Java Platform, Enterprise Edition）和Java是两个相关但不同的概念，它们之间的区别如下：

1. **Java**：
   
   - **Java** 是一种编程<mark>语言</mark>，最初由Sun Microsystems开发，并后来由Oracle维护。
   - Java语言提供了一种跨平台的编程方式，使得开发者可以编写一次代码，然后在不同的操作系统上运行，只需安装适当的Java虚拟机（JVM）。
   - Java主要用于开发各种类型的应用程序，包括桌面应用程序、移动应用程序（使用Android开发工具包）、嵌入式系统、Web应用程序和后端服务器应用程序。

2. **JavaEE**：
   
   - **JavaEE** 是Java<mark>平台</mark>的一个子集，用于开发企业级应用程序。它构建在标准的Java平台之上，提供了一组企业级的API和规范，以支持大规模、分布式和可扩展的应用程序开发。
   - JavaEE包括一系列的规范和API，用于处理事务管理、持久化、消息传递、安全性、Web服务和分布式计算等企业级应用程序的需求。
   - JavaEE应用程序通常部署在JavaEE兼容的应用服务器（如Tomcat、Wildfly、WebLogic、WebSphere等）上，这些服务器提供了JavaEE规范所要求的运行时环境。

因此，Java是一种编程语言，而JavaEE是一种构建企业级应用程序的平台，它在Java语言的基础上提供了额外的功能和API，以满足企业级应用程序的需求。选择使用Java还是JavaEE取决于项目的性质和需求。如果只需要开发简单的应用程序，可能只需要使用Java。但如果需要构建大规模的企业级应用程序，那么JavaEE可能更合适，因为它提供了处理复杂业务逻辑和分布式系统需求的工具和规范。不过需要注意的是，JavaEE在最新的Java开发趋势中逐渐被Jakarta EE所取代。
![Alt text](images/image-2.png)

# Java关键特点和特性

1. **跨平台性（Platform Independence）**：Java是一种<mark>跨平台</mark>的编程语言，也就是说，你可以编写一次Java代码，然后在不同的操作系统上运行，如Windows、Linux、macOS等，只要安装了相应的Java虚拟机（JVM）。这是通过将Java源代码编译为中间字节码（bytecode），然后在JVM上运行字节码来实现的。

2. **面向对象编程（Object-Oriented Programming，OOP）**：Java是一种面向对象的编程语言，它鼓励开发者使用对象、类、继承、封装和多态等OOP概念来构建程序。这有助于提高代码的可重用性和可维护性。

3. **安全性（Security）**：Java具有强大的安全性特性，包括内置的安全性机制，如沙盒环境，可以防止恶意代码执行。这使得Java成为网络和移动应用程序开发的首选语言之一。

4. **自动内存管理（Automatic Memory Management）**：Java具有垃圾回收机制，它可以自动管理内存分配和释放，帮助开发者避免内存泄漏和手动内存管理的烦恼。

5. **丰富的标准库（Rich Standard Library）**：Java附带了一个庞大的标准类库，包含了大量的工具类和API，可以用于处理各种任务，从文件操作到网络通信，再到图形界面开发，都有相应的库可用。

6. **多线程支持（Multithreading Support）**：Java内置了多线程支持，允许程序同时执行多个线程，从而提高了并发性能。

7. **广泛应用领域（Wide Range of Applications）**：Java广泛用于开发各种类型的应用程序，包括桌面应用程序、Web应用程序、移动应用程序（Android应用程序使用Java语言）、企业级应用程序、嵌入式系统等。

8. **开放源代码生态系统（Open Source Ecosystem）**：Java有一个庞大的开发社区和丰富的开源库和框架，使开发者能够更轻松地构建复杂的应用程序。
