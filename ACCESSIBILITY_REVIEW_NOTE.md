# Accessibility Review Note — Week 14: Branded Web Portal

**Name:** Jenna Baligat  **Course:** PC15 Python Programming 2 w/ Lab  **Date:** November 17, 2026
**Project:** Amethyst Learning Portal (Home, About, Programs, Contact)

> Draft prepared from the project's code. Your instructor's own template wasn't included in the
> assignment PDF, so transfer these answers into it. Verify each item yourself before submitting.

## 1. Summary

All four pages extend one `base.html`, so the accessibility features below are built once in the shared
layout and apply to every page automatically. That is a main benefit of template inheritance: fixing
one accessibility problem in `base.html` fixes it across the whole site.

## 2. Checklist

| # | Area | Result | Where / how |
|---|------|--------|-------------|
| 1 | Page language declared | Pass | `<html lang="en">` in `base.html` |
| 2 | Unique, descriptive page titles | Pass | `{% block title %}` overridden on each page (e.g. "About \| Amethyst Learning Portal") |
| 3 | Skip link to main content | Pass | "Skip to main content" link at the top of `base.html`; becomes visible on keyboard focus |
| 4 | Landmarks | Pass | `<header>`, `<nav aria-label="Main navigation">`, `<main id="main">`, `<footer>` |
| 5 | Current page indicated | Pass | `aria-current="page"` on the active nav link, plus a filled-pill style |
| 6 | Heading structure | Pass | One `<h1>` per page, followed by `<h2>`/`<h3>` in order |
| 7 | Keyboard navigation | Pass | All links are native `<a>` elements and reachable by Tab in a logical order |
| 8 | Visible focus indicator | Pass | `:focus-visible` shows a 3px light-purple outline in `style.css` |
| 9 | Colour contrast | Pass (to confirm with a checker) | Body text `#f3effc` on `#120a1f` and muted text `#b3a7d1` on `#120a1f` are well above the 4.5:1 minimum. Re-check with a contrast tool for your screenshots. |
| 10 | Not relying on colour alone | Pass | Active page is shown by `aria-current` and a filled shape, not only by colour |
| 11 | Data table semantics | Pass | Programs table uses `<caption>` (screen-reader only), `<th scope="col">` and `<th scope="row">` |
| 12 | Responsive / zoom | Pass | `viewport` meta, fluid grid, wide table scrolls inside its own container |
| 13 | Reduced motion | Pass | `prefers-reduced-motion` disables transitions |
| 14 | Images / alt text | N/A | The site uses no content images. The "A" logo mark is decorative and hidden with `aria-hidden="true"` |
| 15 | Forms | N/A | No forms on this site |

## 3. Issues found and recommended improvements

1. **Third-party font:** Inter loads from Google Fonts. If offline, the page falls back to the system font, which is still readable.
2. **Contrast verification:** Ratios were estimated from the colour values, not measured. Run the pages through a tool such as the WAVE extension or Chrome Lighthouse and record the score.
3. **Screen reader test:** Not performed. Test with NVDA (Windows) or Narrator and confirm the skip link, landmarks and table are announced correctly.
4. **Future pages:** When forms are added (e.g. login in Week 15), each input needs a visible `<label>` and clear error messages.

## 4. Reflection

Putting the skip link, landmarks, language and focus styles in `base.html` means a new page that
extends it is accessible by default and only has to provide its own headings and content.
