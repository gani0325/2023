const mongoose = require("mongoose");

const BlogSchema = new mongoose.Schema({
    title: {
        type: String,
        required: true,
    },
    description: {
        type: String,
        required: true,
    },
    category: {
        type: String,
        required: true,
    },
    numViews: {
        type: Number,
        default: 0,
    },
    isLiked: {
        type: Boolean,
        required: false,
    },
    isDisliked: {
        type: Boolean,
        required: false,
    },
    likes: [{
        type: mongoose.Schema.Types.ObjectId,
        ref: "User",
    }],
    dislikes: [{
        type: mongoose.Schema.Types.ObjectId,
        ref: "User",
    }],
    image: {
        type: String,
        default:
            "https://tistory1.daumcdn.net/tistory/5027112/attach/f5df7133efd24c339e40102b168855b0"
    },
    author: {
        type: String,
        default: "Admin",
    },
    images : []
}, {
    toJSON: {
        virtuals: true,
    },
    toObject: {
        virtuals: true,
    },
    timestamps: true,
    collection: 'blog'
});

const Blog = mongoose.model("Blog", BlogSchema);
module.exports = Blog;