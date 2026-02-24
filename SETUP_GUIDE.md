# Lenovo Store Alwar - Quick Setup Guide

## Viewing Your Website

### Option 1: View Locally (Easiest)
1. Open the `index.html` file in your web browser
2. The website works immediately with no setup needed

### Option 2: Share with Others Instantly

#### Using Live Server (VS Code)
1. Open the project in VS Code
2. Right-click `index.html`
3. Click "Open with Live Server"
4. Your website opens in the browser with a shareable link

#### Using Python (Terminal)
```bash
cd /Users/ashishjain/lenovo-store-alwar
python3 -m http.server 8000
```
Then visit: `http://localhost:8000`

## Customization Checklist

### 🔴 Required Changes
- [ ] Update phone number (line search for "+919876543210")
- [ ] Update email (search for "info@lenovoalwar.com")
- [ ] Verify address is correct (101, Jai Complex, Alwar)
- [ ] Update business hours if different

### 🟡 Recommended Changes
- [ ] Update Google Maps embed with your actual location
- [ ] Replace hero image with your store photos
- [ ] Add testimonials/reviews section
- [ ] Link to social media (WhatsApp, Facebook, Instagram)

### 🟢 Optional Enhancements
- [ ] Add FAQ section
- [ ] Add customer reviews/testimonials
- [ ] Setup contact form backend
- [ ] Add Google Analytics

## Deploy to a Custom Domain

### Netlify (Free & Easy)
1. Visit https://netlify.com
2. Drag and drop this folder
3. Get a free domain or connect your own
4. Share the link!

### Vercel (Fastest)
```bash
npm i -g vercel
cd /Users/ashishjain/lenovo-store-alwar
vercel
```

### GoDaddy/Domain Provider
Upload files via FTP or use their website builder

## Mobile-First Design Features

✅ Sticky "Call Now" button (bottom right on mobile)
✅ Hamburger menu on small screens
✅ Optimized touch targets
✅ Fast loading on 4G networks
✅ Readable text sizes

## Contact Form Setup

The contact form is currently a placeholder. To make it functional:

### Option 1: Email Service (Recommended)
Use Formspree.io:
1. Go to https://formspree.io
2. Create account with your email
3. Copy their form code
4. Replace the form in `index.html`

### Option 2: WhatsApp Integration
Replace form with WhatsApp button:
```html
<a href="https://wa.me/919876543210?text=Hi, I'm interested in Lenovo products"
   target="_blank" class="btn-green">
   Chat on WhatsApp
</a>
```

## SEO Optimization Tips

1. **Local SEO**
   - Add your store to Google Business Profile
   - Link back from Wikipedia, local directories
   - Use location keywords in content

2. **Technical SEO**
   - Add schema markup for local business
   - Speed up images (use https://tinypng.com)
   - Add meta descriptions

3. **Content**
   - Add blog posts about Lenovo products
   - Create location-specific landing pages
   - Mention local events/partnerships

## Troubleshooting

**Website looks broken?**
- Ensure you're using a modern browser (Chrome, Firefox, Safari, Edge)
- Clear browser cache (Ctrl/Cmd + Shift + Delete)
- Check internet connection

**Images not loading?**
- The current images are from Unsplash CDN
- Replace with your own store photos for better branding

**Contact form not working?**
- Forms need a backend service (see "Contact Form Setup" section)
- For now, "Call Now" button works perfectly

## Next Milestones

1. **Week 1**: Customize all business info, deploy online
2. **Week 2**: Set up Google Business Profile, add to local directories
3. **Week 3**: Start promoting via WhatsApp, local ads
4. **Month 2**: Add customer reviews, setup analytics
5. **Month 3**: Optimize based on visitor data

---

**Need help?** All contact details are in the website footer!
