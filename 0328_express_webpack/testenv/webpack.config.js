const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');


module.exports = {
    mode: "development",
    entry: ['./public/main.js', './public/style/index.css' ],
    output: {
        path: path.resolve(__dirname, "dist"),
        filename: "bundle.js",
    },
    devtool: 'inline-source-map',
    module: {
        rules: [
            {
                test: /\.js$/,
                use: 'babel-loader',
                exclude: /node_modules/
            }, 
            {
                test: /\.css$/i,
                use: ["style-loader", "css-loader"],
            }
            ,
        ]
    },
    plugins: [new HtmlWebpackPlugin(
        {
            template: 'src/index.html'
        }
        
    )]
}