# Structs2的概念和作用

Struts2 是一个流行的开源框架，用于构建企业级Java Web应用程序。它是Apache Software Foundation的一部分，是原始Struts框架的后继者。作为一个Model-View-Controller (MVC)框架，Struts2帮助开发者创建分离关注点的应用，简化了Web应用的开发过程。

>MVC框架（Model-View-Controller框架）是一种广泛使用的软件设计模式，特别是在Web应用程序的开发中。它将应用程序分为三个互相关联的组件：模型（Model）、视图（View）和控制器（Controller）。这种分离帮助开发者组织代码，提高了应用程序的灵活性和可维护性。下面是这三个组件的主要职责：
>
>1. **模型（Model）**：模型组件代表应用程序的数据逻辑。它直接管理数据、逻辑和规则。模型可以响应请求（通常来自控制器），在数据上执行操作，并返回数据的状态。它与数据库直接交互（如有必要）并处理所有数据相关的逻辑。
>
>2. **视图（View）**：视图组件用于呈现数据（即模型）给用户。它是用户界面的一部分。视图只展示数据，不执行任何数据处理或业务逻辑。例如，在Web应用程序中，视图通常是HTML和CSS构成的页面。
>
>3. **控制器（Controller）**：控制器充当模型和视图之间的中介。它接收用户的输入（例如，鼠标点击、键盘输入等），并调用模型和视图的适当组件来处理这些输入。控制器解析用户的输入（例如，通过Web表单提交的数据），处理这些输入，并将其传递给模型组件进行数据处理。
>
>MVC框架的优势在于其清晰的组织结构，有助于分离关注点，使得开发、测试和维护应用程序变得更加简单。不同的开发人员可以独立工作于模型、视图或控制器，这提高了团队合作的效率。此外，由于MVC支持模块化的代码，所以在进行功能更改或设计更新时，只需修改特定的组件，而不需要重写整个应用程序。
>
>很多流行的Web开发框架，如Ruby on Rails、Django（Python）、Spring MVC（Java）和ASP.NET MVC（.NET），都采用了MVC架构。这些框架提供了一套标准化的方法来构建Web应用程序，同时允许足够的灵活性来适应特定的项目需求。

# 在集成开发平台eclipse上配置Struts2框架，学习Struts2编程

在Eclipse集成开发环境（IDE）中配置Struts2框架并开始学习Struts2编程涉及多个步骤。以下是一个基本的指南来帮助你开始：

## 1. 安装Eclipse

首先，确保你已经安装了Eclipse IDE。如果还没有安装，可以从[Eclipse官网](https://www.eclipse.org/downloads/)下载并安装。

## 2. 创建Java Web项目

1. 打开Eclipse，选择 `File` -> `New` -> `Dynamic Web Project`。
2. 输入项目名称。
3. 选择适当的目标运行环境（比如Tomcat服务器）。
4. 点击 `Finish` 创建项目。

## 3. 添加Struts2依赖

你可以通过手动添加JAR文件或使用Maven来添加Struts2依赖。

### 手动添加JAR文件：

1. 下载Struts2的JAR文件。你可以从[Struts官网](https://struts.apache.org/download.cgi)下载。
2. 将下载的JAR文件复制到项目的 `WebContent/WEB-INF/lib` 目录下。

### 使用Maven（推荐）：

1. 右击项目，选择 `Configure` -> `Convert to Maven Project`。
2. 在生成的 `pom.xml` 文件中，添加Struts2的依赖项：
   ```xml
   <dependencies>
       <dependency>
           <groupId>org.apache.struts</groupId>
           <artifactId>struts2-core</artifactId>
           <version>[适当的版本]</version>
       </dependency>
       <!-- 添加其他需要的依赖 -->
   </dependencies>
   ```

## 4. 配置Struts2

1. 在 `WebContent/WEB-INF` 目录下创建一个名为 `struts.xml` 的文件。
2. 在 `struts.xml` 文件中添加基本的Struts2配置：
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE struts PUBLIC
       "-//Apache Software Foundation//DTD Struts Configuration 2.5//EN"
       "http://struts.apache.org/dtds/struts-2.5.dtd">
   <struts>
       <package name="default" extends="struts-default">
           <!-- 配置Action和结果 -->
       </package>
   </struts>
   ```

## 5. 编写第一个Struts2 Action

1. 在 `src` 目录下创建一个新的Java类，比如 `HelloWorldAction`。
2. 在这个类中添加方法和逻辑。例如：
   ```java
   public class HelloWorldAction {
       public String execute() {
           return "SUCCESS";
       }
   }
   ```

## 6. 更新 `struts.xml` 配置

在 `struts.xml` 中配置你的Action：
```xml
<package name="default" extends="struts-default">
    <action name="hello" class="com.yourpackage.HelloWorldAction">
        <result name="SUCCESS">/success.jsp</result>
    </action>
</package>
```

## 7. 创建JSP页面

在 `WebContent` 目录下创建相应的JSP页面，比如 `success.jsp`。

## 8. 运行和测试

1. 配置服务器（如Tomcat）。
2. 将项目部署到服务器上。
3. 在浏览器中访问相应的URL（例如 `http://localhost:8080/YourProjectName/hello`）来测试你的Struts2应用。

## 学习资源

- **官方文档**：参阅[Struts2官方文档](https://struts.apache.org/docs/)，了解更多详细信息和高级概念。
- **在线教程**：网上有很多免费的教程可以帮助你更深入地学习Struts2。

按照这些步骤，你就可以开始在Eclipse中使用Struts2进行开发了。随着你对框架的理解加深，你可以开始探索更高级的功能，如拦截器、标签库、OGNL表达式等。

# 使用 Struts 2 框架实现登录系统

以下是一个基本的指南：

## 1. 环境搭建

确保你的开发环境已经安装了 Java、Servlet 容器（如 Tomcat），以及 Maven 或者是你选择的任何构建工具。

## 2. 引入 Struts 2 依赖

在你的 `pom.xml` 文件中加入 Struts 2 的依赖项。例如：

```xml
<dependency>
    <groupId>org.apache.struts</groupId>
    <artifactId>struts2-core</artifactId>
    <version>2.5.20</version> <!-- 使用最新的稳定版本 -->
</dependency>
```

## 3. 创建 Struts 2 Action 类

登录功能通常需要一个 Action 类来处理用户输入。例如：

```java
public class LoginAction extends ActionSupport {
    private String username;
    private String password;

    // getter 和 setter 方法

    public String execute() {
        // 登录逻辑
        if ("admin".equals(username) && "password".equals(password)) {
            return SUCCESS;
        } else {
            return LOGIN;
        }
    }
}
```

## 4. 配置 Struts.xml

在 `src/main/resources` 目录下创建或编辑 `struts.xml` 文件，定义 Action 映射。例如：

```xml
<struts>
    <package name="default" extends="struts-default">
        <action name="login" class="com.example.LoginAction">
            <result name="success">/welcome.jsp</result>
            <result name="login">/login.jsp</result>
        </action>
    </package>
</struts>
```

## 5. 创建 JSP 页面

创建用于用户输入的 `login.jsp` 和显示登录成功消息的 `welcome.jsp`。

## 6. 配置 web.xml

在 `WEB-INF` 目录下的 `web.xml` 文件中配置 Struts 2 的 `FilterDispatcher`。

## 7. 部署与测试

部署你的应用到 Servlet 容器，并进行测试。

## 注意事项

- 确保所有必要的库都被正确包含在你的项目中。
- 关注安全性，避免常见的安全漏洞，例如 SQL 注入。
- 这只是一个基本示例，实际项目中可能需要更复杂的用户验证和错误处理。

这个过程涵盖了使用 Struts 2 创建基本登录系统的关键步骤。实际实现可能根据你的具体需求有所不同。