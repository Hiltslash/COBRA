const vscode = require('vscode');
const cp = require('child_process');

function activate(context) {
  let disposable = vscode.commands.registerCommand('cobra.runFile', function () {
    const editor = vscode.window.activeTextEditor;
    if (!editor) {
      vscode.window.showErrorMessage('No active editor');
      return;
    }

    const filePath = editor.document.fileName;

    if (!filePath.endsWith('.coil')) {
      vscode.window.showErrorMessage('Not a .coil file.');
      return;
    }

    const terminal = vscode.window.createTerminal("Cobra");
    terminal.show();
    terminal.sendText(`cobra "${filePath}"`);
  });

  context.subscriptions.push(disposable);
}

function deactivate() {}

module.exports = {
  activate,
  deactivate
};
