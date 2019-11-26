const webpack = require('webpack')
const path = require('path')

module.exports = {
  publicPath: process.env.NODE_ENV === 'production'
    ? './static'
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
