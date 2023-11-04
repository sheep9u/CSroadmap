# 举例：最简单的Java程序

是一个Hello World程序，它只是在屏幕上输出"Hello, World!"这个简单的消息。以下是一个基本的Java Hello World程序示例：

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

The `main()` method（方法） is required（必需的） and you will see it in every Java program. Any code inside the `main()` method will be executed.

For now, just remember that every Java program has a `class` name which must <mark>match the filename</mark>, and that every program must contain the `main()` method.

要运行这个程序，你需要安装Java开发工具包（JDK）

You can use the `println()` method to output values or print text in Java.



# 举例：最经典的Java程序

可能会因人而异，但以下是一个非常常见的经典Java程序，用于演示如何从键盘读取用户输入并进行简单的处理：

```java
import java.util.Scanner;

public class ClassicJavaProgram {
    public static void main(String[] args) {
        // 创建一个Scanner对象，用于读取用户输入
        Scanner scanner = new Scanner(System.in);

        // 提示用户输入一个整数
        System.out.print("请输入一个整数: ");

        // 读取用户输入的整数
        int userInput = scanner.nextInt();

        // 处理用户输入，这里简单地打印出用户输入的两倍值
        int result = userInput * 2;
        System.out.println("输入的整数的两倍是: " + result);

        // 关闭Scanner对象
        scanner.close();
    }
}
```

这个程序的功能很简单：

1. 它使用`java.util.Scanner`类创建一个Scanner对象，以便从键盘读取用户输入。

2. 程序要求用户输入一个整数，并将用户输入的整数存储在`userInput`变量中。

3. 然后，程序将用户输入的整数乘以2，并将结果存储在`result`变量中。

4. 最后，程序打印出结果，显示用户输入的整数的两倍值。

要运行这个程序，可以按照之前提到的步骤编译和运行Java程序。用户将被提示输入一个整数，然后程序将返回输入的整数的两倍值。

这个程序展示了Java的一些基本概念，如输入/输出、变量、算术运算和基本的控制流程。这些都是编程中的基础知识。

举例:两数相加

当然，以下是一个简单的Java程序示例，它将两个整数相加并打印结果：

```java
public class Addition {
    public static void main(String[] args) {
        // 定义两个整数
        int num1 = 5;
        int num2 = 7;

        // 计算它们的和
        int sum = num1 + num2;

        // 打印结果
        System.out.println("两个整数的和为：" + sum);
    }
}
```

这个程序的主要部分包括以下几个元素：

- `public class Addition`：定义了一个名为 "Addition" 的公共类。
- `public static void main(String[] args)`：是Java程序的入口点，它指明了程序从哪里开始执行。
- `int num1 = 5;` 和 `int num2 = 7;`：声明并初始化了两个整数变量 `num1` 和 `num2`。
- `int sum = num1 + num2;`：计算了两个整数的和，并将结果存储在 `sum` 变量中。
- `System.out.println("两个整数的和为：" + sum);`：打印了计算结果到控制台。

当你运行这个程序时，它会输出 "两个整数的和为：12"，因为5和7的和是12。这只是一个非常简单的示例，但它演示了Java程序的基本结构和语法。你可以根据需要构建更复杂的Java程序，包括用户输入、条件语句、循环等更多功能。

# Java简介

Java是一种广泛使用的高级编程语言，它具有以下几个关键特点和特性：

1. **跨平台性（Platform Independence）**：Java是一种<mark>跨平台</mark>的编程语言，也就是说，你可以编写一次Java代码，然后在不同的操作系统上运行，如Windows、Linux、macOS等，只要安装了相应的Java虚拟机（JVM）。这是通过将Java源代码编译为中间字节码（bytecode），然后在JVM上运行字节码来实现的。

2. **面向对象编程（Object-Oriented Programming，OOP）**：Java是一种面向对象的编程语言，它鼓励开发者使用对象、类、继承、封装和多态等OOP概念来构建程序。这有助于提高代码的可重用性和可维护性。

3. **安全性（Security）**：Java具有强大的安全性特性，包括内置的安全性机制，如沙盒环境，可以防止恶意代码执行。这使得Java成为网络和移动应用程序开发的首选语言之一。

4. **自动内存管理（Automatic Memory Management）**：Java具有垃圾回收机制，它可以自动管理内存分配和释放，帮助开发者避免内存泄漏和手动内存管理的烦恼。

5. **丰富的标准库（Rich Standard Library）**：Java附带了一个庞大的标准类库，包含了大量的工具类和API，可以用于处理各种任务，从文件操作到网络通信，再到图形界面开发，都有相应的库可用。

6. **多线程支持（Multithreading Support）**：Java内置了多线程支持，允许程序同时执行多个线程，从而提高了并发性能。

7. **广泛应用领域（Wide Range of Applications）**：Java广泛用于开发各种类型的应用程序，包括桌面应用程序、Web应用程序、移动应用程序（Android应用程序使用Java语言）、企业级应用程序、嵌入式系统等。

8. **开放源代码生态系统（Open Source Ecosystem）**：Java有一个庞大的开发社区和丰富的开源库和框架，使开发者能够更轻松地构建复杂的应用程序。

Java <mark>owned by Oracle, created in 1995</mark>. 它的设计目标是写一次，到处运行，这个目标一直延续至今，使得Java在众多领域都有广泛的应用。总之，Java是一门强大且多用途的编程语言，适用于各种不同类型的软件开发项目。

继续关于Java的简介：

9. **Java平台的组成**：Java平台由多个组成部分构成，其中最重要的是：
   
   - **Java编程语言**：Java编程语言本身，它定义了语法、数据类型和控制结构等，开发者使用它来编写应用程序的源代码。
   
   - **Java虚拟机（JVM）**：JVM是Java平台的核心组件，负责将Java字节码翻译成特定平台的本地机器代码。不同操作系统上都有不同的JVM实现，但它们都能够执行相同的Java字节码，从而实现跨平台性。
   
   - **Java标准库（Java Standard Library）**：也称为Java API（Application Programming Interface），包括了众多的类和方法，开发者可以使用它们来完成各种任务，如输入/输出、数据结构、网络通信、图形界面等。

10. **Java的版本**：Java不断发展，每个新版本都引入了新特性和改进。自Java 5以来，Java平台引入了许多重要的语言和库特性，如泛型、枚举、注解、Lambda表达式等。此外，Java的版本发布遵循一定的时间表，通常每年发布一个主要版本，以确保开发者能够及时获得最新的功能和安全更新。

11. **Java的应用领域**：由于其多功能性和稳定性，Java被广泛用于各种应用领域，包括但不限于：
    
    - **企业级应用**：Java EE（Java Platform, Enterprise Edition）提供了用于开发大型、分布式和高可用性企业应用的工具和规范。
    
    - **桌面应用**：Java可以用于开发图形用户界面（GUI）应用，尤其是使用JavaFX等技术。
    
    - **移动应用**：虽然Android应用使用Java编程语言，但它使用了自己的API和框架。
    
    - **Web应用**：Java可以用于构建服务器端应用程序，如Web应用的后端，常用的框架包括Spring和Servlet。
    
    - **嵌入式系统**：Java可以用于开发嵌入式和物联网（IoT）设备的应用程序。

12. **学习和开发工具**：为了学习和开发Java应用程序，开发者可以使用各种集成开发环境（IDE）如Eclipse、IntelliJ IDEA和NetBeans等，以及文本编辑器。此外，Java社区提供了大量的教程、书籍和在线资源，以帮助开发者入门和提高他们的Java编程技能。

总之，Java是一门功能强大、跨平台、安全可靠的编程语言，适用于多种应用领域，是编程世界中的一颗耀眼的明星。无论你是初学者还是有经验的开发者，学习和掌握Java都能为你提供广泛的职业机会和编程技能。

# Java能用来做什么

Java is a popular programming language.

Java是一种强大的、多用途的编程语言，广泛应用于各种领域和用途。以下是Java常见的用途：

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

总之，Java是一种多功能的编程语言，适用于各种不同领域，从移动应用到企业级应用，从大数据处理到科学研究，都有广泛的应用。其跨平台性和可扩展性使其成为许多开发者的首选语言之一。

# 编译与Java程序运行关系

```
       Java源文件（.java文件）
                |
                | java编译器即javac.exe
                |
                V
      Java字节码文件（.class文件）
                |
                V
      由解释执行器即（java.exe）
   将字节码文件加载到Java虚拟机（jvm）————————>字节码文件就会在Java虚拟机中执行
```

# 平台无关

无论哪种语言写的程序，都需要OS（操作系统）和CPU（处理器）来完成程序的运行。因此这里的平台是由OS和CPU所构成。

<mark>每个平台都会形成自己独特的机器指令</mark>，相同CPU和不同的操作系统所形成的平台的机器指令可能是不同的，例如，某种平台可能用8位序列代码00001111表示加法指令，用10000001表示减法指令，而另一种平台可能用8位序列代码10101010表示加法指令，用10010011表示减法指令。

> C/C++程序依赖平台:
> 
> C/C++有个缺点，只能对特定的处理器（Central Processing Units，CPU）芯片进行编译。
> 
> C/C++源程序所在的特定平台，对其源文件进行编译、链接，生成机器指令，即根据当前平台的机器指令生成可执行文件，那么可以在任何与当前平台相同的平台上运行这个可执行文件，但是不能保证它在所有的平台上都能正确的执行。

Java可以在平台之上再提供个<mark>Java运行环境</mark>（由Java虚拟机、类库、一些核心文件组成），Java虚拟机把Java源程序编译成称为字节码的“中间代码”，并负责将字节码翻译成虚拟机所在平台的机器码，并交给此平台运行该机器码

# Java Data Type

`byte`, `short`, `int`, `long`, `float`, `double`, `boolean` and `char` are called: primitive data types.（原始数据类型）

Java has a `boolean` data type, which can store `true` or `false` values.



Non-Primitive Data Types（非原始数据类型）- such as "String", Arrays and Classes（字符串、数组、类）
Non-primitive data types are called reference types（引用类型） because they refer to objects.（因为他们引用对象）

> The main difference between primitive and non-primitive data types are:
> 
> （1）Primitive types are predefined （预定义的） (already defined) in Java. Non-primitive types are created by the programmer and is not defined by Java (except for String).
> 
> （2）Non-primitive types can be used to call methods to perform certain operations（可用于调用方法来执行某些操作）, while primitive types cannot.
> 
> （3）A primitive type has always a value, while（而） non-primitive types can be null.
> 
> （4）A primitive type starts with a lowercase letter（小写字母开头）, while non-primitive types starts with an uppercase letter.

# Java Type Casting

> Java 类型转换

Widening Casting 加宽铸造

```java
public class Main {
  public static void main(String[] args) {
    int myInt = 9;
    double myDouble = myInt; // Automatic casting: int to double

    System.out.println(myInt);      // Outputs 9
    System.out.println(myDouble);   // Outputs 9.0
  }
}
```

Narrowing Casting 缩小铸造

```java
public class Main {
  public static void main(String[] args) {
    double myDouble = 9.78d;
    int myInt = (int) myDouble; // Manual casting: double to int

    System.out.println(myDouble);   // Outputs 9.78
    System.out.println(myInt);      // Outputs 9
  }
}
```

# Java If ... Else

Use the `else` statement to specify a block of code to be executed if the condition is `false`.

```java
if (condition) {
  // block of code to be executed if the condition is true
} else {
  // block of code to be executed if the condition is false
}
```

Use the `else if` statement to specify a new condition if the first condition is `false`.

```java
if (condition1) {
  // block of code to be executed if condition1 is true
} else if (condition2) {
  // block of code to be executed if the condition1 is false and condition2 is true
} else {
  // block of code to be executed if the condition1 is false and condition2 is false
}
```

# English

Declaring (Creating) Variables 声明（创建）变量

To create a variable, you must specify the type and assign it a value 指定类型并为其赋值
