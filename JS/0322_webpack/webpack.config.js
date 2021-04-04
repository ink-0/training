const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
module.exports = {
  mode: 'development',
  devtool:'inline-source-map',
  entry: './src/app.js',
  output: {
      path: path.resolve(__dirname, 'dist'),
      filename: 'bundle.js',
  },
  module: {
      rules: [{
          test: /\.js$/,
          exclude: /node_modules/,
          use: {
              loader: 'babel-loader'
          }
      }, ],
    },
    plugins: [new HtmlWebpackPlugin(
        {
            template: 'src/app.html'
        }
    )]
};
