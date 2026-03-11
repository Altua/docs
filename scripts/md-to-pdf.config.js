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
      top: "18mm",
      right: "16mm",
      bottom: "18mm",
      left: "16mm",
    },
    printBackground: true,
  },
};
