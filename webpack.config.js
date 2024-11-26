const path = require('path');

module.exports = {
  entry: './assets/script/index.js', // Main JS entry point
  output: {
    filename: 'bundle.js', // Output bundled file
    path: path.resolve(__dirname, 'apps/static/src/js'), // Correct output path
  },
  module: {
    rules: [
      {
        test: /\.css$/, // Handle .css files
        use: [
          'style-loader', // Inject styles into DOM
          'css-loader',   // Resolve CSS imports
          'postcss-loader', // Use PostCSS to process Tailwind
        ],
      },
    ],
  },
  devServer: {
    contentBase: './apps/static', // Serve static files from this directory
    hot: true,  // Enable hot module replacement
  },
  mode: 'development', 
};
