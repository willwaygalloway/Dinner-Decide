# Dinner Decide

A small web app for two people to agree the week's dinners, then get the shopping list.

**Use it:** https://willwaygalloway.github.io/Dinner-Decide/

## How it works

1. Tap **+ New week** and say how many evenings you're out.
2. Each of you ticks the meals you'd happily eat. You can't see each other's picks until you've both finished.
3. Meals you both picked become the week's dinners, spread across the carbs (pasta, rice, potato and so on).
4. On any dinner, choose **Leftovers** (covers another night), **Freeze extra** or **From freezer**.
5. The **Shop** tab lists the ingredients. Cross off what's in the cupboard and copy the rest.

## Two ways to pick

- **A phone each:** you send your picks to each other as a link (WhatsApp, text, anything). Opening the link adds them.
  Use **Send meals** on the Meals tab to set up the second phone.
- **One shared phone:** pick, tap Done, pass the phone over.

## Where your data lives

Everything is saved in your browser on your own phone. Nothing is sent to a server, and links carry
their data inside the link itself. Use **Back up** on the Meals tab now and then, because clearing your
browser data deletes it. Adding the page to your Home Screen helps your phone keep it.

## For developers

- `index.html` is the app. It is also published as a Claude artifact, where it uses Claude's shared
  database for live syncing between two phones. Outside Claude it uses browser storage instead.
- `docs/index.html` is the GitHub Pages copy. Rebuild it after changing `index.html`:

  ```
  python3 scripts/build_pages.py
  ```
