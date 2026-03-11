const fs = require("fs");
const path = require("path");

const logoPath = path.join(process.cwd(), "logo", "logo-grunt.svg");
const logoSvg = fs.readFileSync(logoPath, "utf8");
const logoDataUri = `data:image/svg+xml;charset=utf-8,${encodeURIComponent(
  logoSvg
)}`;

module.exports = {
  basedir: process.cwd(),
  stylesheet: ["./scripts/md-to-pdf.css"],
  marked_options: {
    gfm: true,
    headerIds: false,
    mangle: false,
  },
  pdf_options: {
    format: "A4",
    margin: {
      top: "24mm",
      right: "16mm",
      bottom: "18mm",
      left: "16mm",
    },
    printBackground: true,
    displayHeaderFooter: true,
    headerTemplate: `
      <style>
        .pdf-header {
          width: 100%;
          padding: 0 16mm;
          box-sizing: border-box;
          text-align: right;
        }

        .pdf-header img {
          width: 96px;
          height: auto;
          margin-top: 2mm;
        }
      </style>
      <div class="pdf-header">
        <img src="${logoDataUri}" alt="Grunt logo" />
      </div>
    `,
    footerTemplate: `<div></div>`,
  },
};
