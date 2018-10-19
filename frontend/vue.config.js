const webpack = require('webpack')
const path = require('path')

module.exports = {
  baseUrl: process.env.NODE_ENV === 'production'
    ? '/{{ BASE_URL }}static'
    : '/',
  // assetsDir: 'static',
  outputDir: '../static',
  lintOnSave: true,
  runtimeCompiler: true,
  configureWebpack: {
    resolve: {
      alias: {
        '@': path.resolve(__dirname, 'src')
      }
    }
  }
}
