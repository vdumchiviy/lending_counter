/* eslint-disable */
const path = require('path')

/**
 * Configuration file for VS Code Vandelay extension.
 * https://github.com/ericbiewener/vscode-vandelay#configuration
 */

module.exports = {
  // This is the only required property. At least one path must be included.
  includePaths: [
    path.join(__dirname, 'app'),
    path.join(__dirname, 'etc'),
    path.join(__dirname, 'res'),
    path.join(__dirname, 'static'),
  ],
}
