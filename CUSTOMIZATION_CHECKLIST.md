# Lenovo Store Alwar - Customization Checklist

Complete this checklist to make the website 100% yours!

## ✅ Business Information

- [ ] **Phone Numbers**
  - Find: `+919876543210`
  - Replace with: Your actual phone number
  - Appears in: Navigation, Contact section, Header button

- [ ] **Email Address**
  - Find: `info@lenovoalwar.com`
  - Replace with: Your actual email
  - Appears in: Footer, Contact form

- [ ] **Store Address**
  - Find: `101, Jai Complex, Alwar, Rajasthan 301001`
  - Verify: This is correct
  - Location: About section, Footer, Contact section

- [ ] **Business Hours**
  - Current: Mon-Sat 10 AM - 8 PM, Sun 11 AM - 7 PM
  - Update if different
  - Location: Contact section

## 📍 Google Maps

- [ ] Get your business location embed
  1. Go to Google Maps
  2. Search for your store
  3. Click "Share" → "Embed map"
  4. Copy the iframe code
  5. Replace starting at line ~650 in `index.html`

## 📸 Images & Branding

### Hero Section (Line ~130)
- [ ] Current: Laptop from Unsplash
- [ ] Replace with: Your store/products photo
- [ ] Recommended: 1920x1080px, high quality

### Product Cards (Lines 220-270)
- [ ] ThinkPad: Keep or replace with ThinkPad image
- [ ] Legion: Keep or replace with Gaming image
- [ ] Yoga: Keep or replace with Yoga image
- [ ] IdeaPad: Keep or replace with IdeaPad image

### About Section (Line ~615)
- [ ] Current: Team photo
- [ ] Replace with: Your team photo or store interior

## 🎨 Brand Customization

- [ ] Logo: Replace "LENOVO Alwar" with your actual branding
  - Location: Line ~82 (Navigation)
  
- [ ] Colors: Already using Lenovo official colors
  - Blue: #0094D3
  - Can customize in style tags (Lines ~17-35)

## 📞 Contact Form Integration

### Option A: Formspree Setup (Recommended)
- [ ] Create account at https://formspree.io
- [ ] Get your form endpoint
- [ ] Update form action at line ~700

### Option B: Google Forms
- [ ] Create Google Form for quotes
- [ ] Get embed code
- [ ] Add to Contact section

### Option C: WhatsApp Integration
- [ ] Update phone number in quote button
- [ ] Form link will open WhatsApp

## 🔗 Links to Add

### Social Media
- [ ] Add Facebook page link (Footer)
- [ ] Add Instagram link (Footer)
- [ ] Add WhatsApp chat link
- [ ] Add YouTube channel link

### Relevant Links
- [ ] Lenovo official website
- [ ] Support/warranty page
- [ ] Blog or news section
- [ ] Service center details

## 📱 Mobile Testing

- [ ] Test on iPhone/Safari
- [ ] Test on Android/Chrome
- [ ] Test on tablet
- [ ] Verify "Call Now" button works
- [ ] Check menu opens/closes properly

## 🚀 Pre-Deployment Checklist

- [ ] All phone numbers verified
- [ ] All emails correct
- [ ] Address is accurate
- [ ] Images loading properly
- [ ] Links are working
- [ ] Mobile responsive
- [ ] Contact form working
- [ ] Google Maps embedded

## 📊 Post-Deployment Setup

- [ ] Google Business Profile created
- [ ] Google Analytics added
- [ ] Search Console (Google) connected
- [ ] Local directories updated (Justdial, MapMyIndia, etc.)
- [ ] 404 error page configured
- [ ] Backup created
- [ ] SSL certificate active (https)

## 🎯 Content Additions (Future)

- [ ] Customer testimonials/reviews
- [ ] FAQ section
- [ ] Service center details
- [ ] Warranty information
- [ ] EMI/Finance options
- [ ] Latest product launches
- [ ] Special offers section
- [ ] Partnership logos

## 🔐 Security & Performance

- [ ] Cloudflare protection enabled
- [ ] Auto-update security headers
- [ ] Cache optimization
- [ ] Lazy load images
- [ ] SEO meta tags complete
- [ ] Mobile page speed > 90
- [ ] Desktop page speed > 90

## 📞 Quick Customization Guide

### Find & Replace in VS Code
1. Press `Ctrl+H` (Windows) or `Cmd+H` (Mac)
2. Find: `+919876543210`
3. Replace with: Your phone number
4. Click "Replace All"

Repeat for:
- Email: `info@lenovoalwar.com`
- Address: `101, Jai Complex, Alwar`
- Hours: Update in contact section

### Test Changes
1. Save the file
2. Open in browser (F5 to refresh)
3. Check mobile view (DevTools → Toggle mobile)

---

**Status**: _____ / 21 items complete

**Last Updated**: _____________

**Notes**: ________________________________________
