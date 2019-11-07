"use strict";
const path = require("path");
const chalk = require("chalk");
const yosay = require("yosay");
const Generator = require("yeoman-generator");
const loadMethodUrl = "Web portal";
const loadMethodFS = "Local filesystem";

module.exports = class extends Generator {
  prompting() {
    // Have Yeoman greet the user.
    this.log(
      yosay("Welcome to gradefast interactive. This utility allows you to create a gradefast project quickly")
    );

    const prompts = [
      {
        type: "input",
        name: "projectName",
        message: "Project name (no spaces): ",
        default: "gradefast-project"
      },
      {
        type: "input",
        name: "themeName",
        message: "Theme name (no spaces): ",
        default: "RapidRescue"
      },
      {
        type: "input",
        name: "taskName",
        message: "Task name (no spaces): ",
        default: "task0"
      },
      {
        type: "list",
        name: "loadMethod",
        message: "From where do you want to fetch submissions? ",
        choices: [loadMethodUrl, loadMethodFS]
      },
    ];

    return this.prompt(prompts).then(props => {
      // To access props later use this.props.someAnswer;
      this.props = props;
      console.log(props);
    });
  }

  writing() {
    let taskName = this.props.taskName;
    let camelCaseTestName = taskName.charAt(0).toUpperCase() 
    + taskName.slice(1) + 'Test';

    let method = '';
    if (this.props.loadMethod == loadMethodUrl) {
      method = 'url';
    }
    else if (this.props.loadMethod == loadMethodFS) {
      method = 'fs';
    }

    this.fs.copyTpl(
      this.templatePath(`main_${method}.py`),
      this.destinationPath(path.join(this.props.projectName, "main.py")),
      { taskName: taskName, 
        themeName: this.props.themeName,
        camelCaseTestName: camelCaseTestName,
        lowerCaseTaskName: this.props.taskName.toLowerCase()
      }
    );

    this.fs.copyTpl(
      this.templatePath("test.py"),
      this.destinationPath(path.join(this.props.projectName, "test.py")),
      { camelCaseTestName: camelCaseTestName}
    );
  }

  // install() {
  //   this.installDependencies();
  // }
};
