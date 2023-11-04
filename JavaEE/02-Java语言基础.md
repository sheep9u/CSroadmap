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

<table>
  <tr>
   <th>
    编译工具
    </th>
   <th>
   执行工具
   </th>
  </tr>
  <tr>
   <td>
   javac.exe
   </td>
   <td>
   java.exe
   </td>
  <tr>
</table>

编译与Java程序运行关系：

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
