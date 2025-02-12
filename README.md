# CMPT 419, Spring 2025, Human- and Data-centric AI

*Last updated: Jan 5, 2025*

This is the GitHub homepage for Prof. Nick Vincent's CMPT 419 course in Spring 2025.

We'll use this for sharing any publicly-available course content. We may use Coursys or other software for assignment submissions, internal documents, etc.

For now, the main contents of the repo are a draft outline. This will be updated periodically.

## Outline

You can find the course outline [here](http://www.sfu.ca/outlines.html?2025/spring/cmpt/419/d200).

## Syllabus and Course Content

You can visit the GitHub pages static site [here](https://nickmvincent.github.io/cmpt419_spring2025/).

If there's anything you're looking for you can't find there, check the CourSys homepage -- all internal-facing content is there (lecture recordings, notes, etc.)

You can find the syllabus in this repo ([`syllabus.md`](https://github.com/nickmvincent/cmpt419_spring2025/blob/main/syllabus.md)). The syllabus file describe the overall structure of the course and course policies.

You can find the reading assignments in [`CourseReadings.md`](https://github.com/nickmvincent/cmpt419_spring2025/blob/main/readings/CourseReadings.md). Remember that readings may be updated so you should glance at this file weekly.

You can also find "late-breaking links" in [`OptionalLateBreakingLinks.md`](https://github.com/nickmvincent/cmpt419_spring2025/blob/main/readings/OptionalLateBreakingLinks.md). This is where I will post papers, news, blogs, etc. that come up during our class term. You can also submit content to this file to share with your classmates!

I will post coding assignments here as the semester goes in. The GitHub will list the requirements and grading scheme. Submission instructions, deadlines, etc. will be available via CourSys.

## Building the site

Right now, the markdown files in assignments, misc_materials, readings, and the ./syllabus.md file can be written to a static website in `/docs` (for easy GitHub pages use) by running

`python generate_website.py`

or

`uv run generate_website.py` if using uv, as I did.

This website will also generate links to all PDF files in slides_pdfs.

To view slides course code, you'll need to visit slides_src manually.
