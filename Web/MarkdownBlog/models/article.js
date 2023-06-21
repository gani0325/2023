const mongoose = require("mongoose");
const { marked } = require("marked");
const slugify = require("slugify");
const createdDomPurify = require("dompurify");
const { JSDOM } = require("jsdom");
const dompurify = createdDomPurify(new JSDOM().window);

const articleSchema = new mongoose.Schema({
  title: {
    type: String,
    required: true,
  },
  description: {
    type: String,
  },
  markdown: {
    type: String,
    required: true,
  },
  createdAt: {
    type: Date,
    default: Date.now,
  },

  slug: {
    type: String,
    requied: true,
    unique: true,
  },
  sanitizedHtml: {
    type: String,
    requied: true,
  },
});

articleSchema.pre("validate", function (next) {
  // title 명으로 넘어가기
  if (this.title) {
    this.slug = slugify(this.title, { lower: true, strict: true });
  }

  if (this.markdown) {
    this.sanitizedHtml = dompurify.sanitize(marked(this.markdown));
  }
  next();
});

module.exports = mongoose.model("Article", articleSchema);
