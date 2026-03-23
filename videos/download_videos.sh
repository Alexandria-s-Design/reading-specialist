#!/bin/bash
cd "$(dirname "$0")"

OPTS="--remote-components ejs:github -f best[height<=720]/best --no-overwrites"

# Sight Words A-I
yt-dlp $OPTS -o "JH_JR_Sight_Words_Level_A.%(ext)s" "https://www.youtube.com/watch?v=rJePmr-1tfY" 2>&1 | tail -1
yt-dlp $OPTS -o "JH_JR_Sight_Words_Level_B.%(ext)s" "https://www.youtube.com/watch?v=j01nQTtQSOE" 2>&1 | tail -1
yt-dlp $OPTS -o "JH_JR_Sight_Words_Level_C.%(ext)s" "https://www.youtube.com/watch?v=fLGKulK-TSM" 2>&1 | tail -1
yt-dlp $OPTS -o "JH_JR_Sight_Words_Level_D.%(ext)s" "https://www.youtube.com/watch?v=dQswizOXvis" 2>&1 | tail -1
yt-dlp $OPTS -o "JH_JR_Sight_Words_Level_E.%(ext)s" "https://www.youtube.com/watch?v=CSlcFfUIQuw" 2>&1 | tail -1
yt-dlp $OPTS -o "JH_JR_Sight_Words_Level_F.%(ext)s" "https://www.youtube.com/watch?v=ztkVwKS9a2s" 2>&1 | tail -1
yt-dlp $OPTS -o "JH_JR_Sight_Words_Level_G.%(ext)s" "https://www.youtube.com/watch?v=4y4BRm654wQ" 2>&1 | tail -1
yt-dlp $OPTS -o "JH_JR_Sight_Words_Level_H.%(ext)s" "https://www.youtube.com/watch?v=P7AzxnPeXEY" 2>&1 | tail -1
yt-dlp $OPTS -o "JH_JR_Sight_Words_Level_I.%(ext)s" "https://www.youtube.com/watch?v=AO_7t9EkCtg" 2>&1 | tail -1

# Onsets and Rimes 1-5
yt-dlp $OPTS -o "JH_JR_Onsets_Rimes_Set_1.%(ext)s" "https://www.youtube.com/watch?v=Og9YaJeToZ0" 2>&1 | tail -1
yt-dlp $OPTS -o "JH_JR_Onsets_Rimes_Set_2.%(ext)s" "https://www.youtube.com/watch?v=h8G9dGzq--U" 2>&1 | tail -1
yt-dlp $OPTS -o "JH_JR_Onsets_Rimes_Set_3.%(ext)s" "https://www.youtube.com/watch?v=hFBu8wkO_fM" 2>&1 | tail -1
yt-dlp $OPTS -o "JH_JR_Onsets_Rimes_Set_4.%(ext)s" "https://www.youtube.com/watch?v=xFqzBxQvMds" 2>&1 | tail -1
yt-dlp $OPTS -o "JH_JR_Onsets_Rimes_Set_5.%(ext)s" "https://www.youtube.com/watch?v=pNHM1IpL6iI" 2>&1 | tail -1

# Other videos
yt-dlp $OPTS -o "JH_JR_Letter_Formation.%(ext)s" "https://www.youtube.com/watch?v=Yj1TwQywaIE" 2>&1 | tail -1
yt-dlp $OPTS -o "JR_Stepping_Together.%(ext)s" "https://www.youtube.com/watch?v=q-yiiG42tQ4" 2>&1 | tail -1
yt-dlp $OPTS -o "JR_Making_Words_Demo.%(ext)s" "https://youtu.be/6nvXWyUhhe8" 2>&1 | tail -1
yt-dlp $OPTS -o "JR_Updated_Procedures.%(ext)s" "https://youtu.be/j0PPFjjO_W4" 2>&1 | tail -1
yt-dlp $OPTS -o "RISE_Rime_Magic.%(ext)s" "https://youtu.be/1gTbHTPMO9U" 2>&1 | tail -1

# Vimeo
yt-dlp $OPTS -o "JR_Webinar.%(ext)s" "https://vimeo.com/1080584934" 2>&1 | tail -1

echo "=== ALL DOWNLOADS COMPLETE ==="
ls -lh *.mp4 2>/dev/null
