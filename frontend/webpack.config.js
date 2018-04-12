const output = process.env.DEBUG ? 'build-dev.js' : 'build.js'

module.exports = {
  // entry point of our application
  entry: './src/main.js',
  // where to place the compiled bundle
  output: {
    path: __dirname,
    filename: '../static/js/' + output
  },
  module: {
    // `loaders` is an array of loaders to use.
    // here we are only configuring vue-loader
    loaders: [
      {
        test: /\.vue$/, // a regex for matching all files that end in `.vue`
        loader: 'vue-loader' // loader to use for matched files
      },
      {
        test: /\.jsx?$/,
        loader: 'babel-loader',
        exclude: /node_modules/,
        query: {
          presets: ['es2015']
        }
      }
    ]
  },
  devtool: '#source-map'
}