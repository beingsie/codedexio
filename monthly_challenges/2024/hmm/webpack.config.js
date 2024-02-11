const path = require("path");
const BrowserSyncPlugin = require("browser-sync-webpack-plugin");

module.exports = {
  entry: "./src/index.js",
  output: {
    path: path.resolve(__dirname, "dist"),
    filename: "bundle.js",
  },
  resolve: {
    fallback: {
      path: require.resolve("path-browserify"),
    },
  },
  devServer: {
    static: [
      path.resolve(__dirname, "dist"), // Serve files from the dist directory
      path.resolve(__dirname, "dist/css"), // Serve files from the public directory
      path.resolve(__dirname, "src"), // Serve files from the public directory
      
    ],
    hot: true,
    historyApiFallback: true, // Serve index.html for any 404 responses
  },
  plugins: [
    new BrowserSyncPlugin({
      host: "localhost",
      port: 3000,
      proxy: "http://localhost:8080/",
      files: ["./dist/css/*.css", "./dist/*.js"], // Files to watch for changes
      reloadDelay: 100, // Delay in milliseconds to wait after changes
    }),
  ],
  module: {
    rules: [
      {
        test: /\.scss$/,
        use: ["style-loader", "css-loader", "postcss-loader", "sass-loader"],
      },
    ],
  },
  mode: "development", // Switch to development mode for live reloading
};
