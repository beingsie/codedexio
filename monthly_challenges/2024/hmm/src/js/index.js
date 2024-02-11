// Import Lodash
import _ from "lodash";

// Import the Sass file
import "../scss/style.scss";

// HTML content
function component() {
  const element = document.createElement("div");

  // Lodash, now imported by this script
  element.innerHTML = _.join(["Hello", "webpack"], " ");

  return element;
}

// Add html content to html body
document.body.appendChild(component());
