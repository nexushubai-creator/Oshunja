#!/bin/bash

# Batch Procedure Conversion Script
# Converts all procedure HTML files to labiaplasty.html template structure

TEMPLATE="/home/jmatthewlee/claude-test/pages/procedures/pelvic-intimate/labiaplasty.html"
LOG_FILE="/home/jmatthewlee/claude-test/conversion.log"

echo "=== Procedure Conversion Script ===" | tee $LOG_FILE
echo "Started: $(date)" | tee -a $LOG_FILE
echo "" | tee -a $LOG_FILE

# Files already converted
echo "ALREADY CONVERTED:" | tee -a $LOG_FILE
echo "  ✓ pages/facial/botox.html" | tee -a $LOG_FILE
echo "  ✓ pages/procedures/facial/botox.html" | tee -a $LOG_FILE
echo "  ✓ pages/procedures/facial/juvederm.html" | tee -a $LOG_FILE
echo "  ✓ pages/procedures/facial/microneedling.html" | tee -a $LOG_FILE
echo "" | tee -a $LOG_FILE

# Define arrays of files to convert by category
declare -a FACIAL=(
  "prp-facial.html"
  "botox-enhanced.html"
  "botox-luxury.html"
)

declare -a BODY=(
  "prp-breast-lift.html"
  "liposuction-360-180.html"
  "renuvion-abdomen.html"
  "liposuction-360.html"
  "renuvion-arms.html"
  "renuvion-back.html"
  "renuvion-neck.html"
)

declare -a HAIR=(
  "laser-hair-removal.html"
  "prp-hair-restoration.html"
)

declare -a PELVIC_INTIMATE=(
  "clitoral-hood-reduction.html"
  "perineoplasty.html"
  "anal-skin-removal.html"
  "vaginoplasty.html"
  "vulvar-vaginal-cysts-warts.html"
  "hymenoplasty.html"
  "lichen-sclerosus-treatment.html"
  "labial-puff.html"
)

declare -a PELVIC_REPRODUCTIVE=(
  "myomectomy.html"
  "annual-exam.html"
  "endometrial-ablation.html"
  "colposcopy.html"
  "thinprep-pap.html"
  "laparoscopy.html"
  "hysteroscopy.html"
  "hysterectomy.html"
)

declare -a SEXUAL_HEALTH=(
  "o-shot.html"
  "clit-shot.html"
  "bioidentical-hormones-women.html"
  "shockwave-therapy.html"
  "testosterone-optimization.html"
  "emsella-chair.html"
  "bioidentical-hormones-men.html"
  "menopause-management.html"
  "p-shot.html"
)

declare -a WELLNESS=(
  "mounjaro.html"
  "ozempic.html"
  "dietetics.html"
  "iv-therapy.html"
  "salt-blocks.html"
  "sauna.html"
  "cold-plunge.html"
  "wellness-coaching.html"
  "metabolic-health-testing.html"
)

# Counter
TOTAL=0
CONVERTED=0

# Function to create Claude Code prompt for a batch of files
generate_batch_prompt() {
  local category=$1
  shift
  local files=("$@")

  echo ""
  echo "=============================================="
  echo "BATCH: $category"
  echo "=============================================="
  echo ""
  echo "Convert these ${#files[@]} files to labiaplasty.html template:"
  echo ""

  for file in "${files[@]}"; do
    echo "  - pages/procedures/$category/$file"
    ((TOTAL++))
  done

  echo ""
  echo "Use template: pages/procedures/pelvic-intimate/labiaplasty.html"
  echo ""
  echo "Required structure:"
  echo "  1. Header with dropdown navigation"
  echo "  2. Procedure Hero with breadcrumb"
  echo "  3. Quick Info Bar (⏱💤🏠✨)"
  echo "  4. Overview (3 paragraphs)"
  echo "  5. How It Works (4 steps + info box)"
  echo "  6. Benefits & Results (6 cards + timeline)"
  echo "  7. Candidates (2-column + warning)"
  echo "  8. Recovery (4 phases + tips + warning)"
  echo "  9. Complementary Treatments (4 cards + note)"
  echo "  10. FAQ (details/summary)"
  echo "  11. CTA section"
  echo "  12. Footer (4 columns)"
  echo "  13. WhatsApp button"
  echo "  14. Structured Data JSON-LD"
  echo ""
  echo "Preserve procedure-specific content!"
  echo "Phone: +1 (876) 611-5100"
  echo "Address: 10-12 Oxford Road, Kingston 5, Jamaica"
  echo ""
}

# Generate prompts for each category
{
  echo "FILES TO CONVERT - BY CATEGORY"
  echo "================================"
  echo ""

  if [ ${#FACIAL[@]} -gt 0 ]; then
    generate_batch_prompt "facial" "${FACIAL[@]}"
  fi

  if [ ${#BODY[@]} -gt 0 ]; then
    generate_batch_prompt "body" "${BODY[@]}"
  fi

  if [ ${#HAIR[@]} -gt 0 ]; then
    generate_batch_prompt "hair" "${HAIR[@]}"
  fi

  if [ ${#PELVIC_INTIMATE[@]} -gt 0 ]; then
    generate_batch_prompt "pelvic-intimate" "${PELVIC_INTIMATE[@]}"
  fi

  if [ ${#PELVIC_REPRODUCTIVE[@]} -gt 0 ]; then
    generate_batch_prompt "pelvic-reproductive" "${PELVIC_REPRODUCTIVE[@]}"
  fi

  if [ ${#SEXUAL_HEALTH[@]} -gt 0 ]; then
    generate_batch_prompt "sexual-health" "${SEXUAL_HEALTH[@]}"
  fi

  if [ ${#WELLNESS[@]} -gt 0 ]; then
    generate_batch_prompt "wellness" "${WELLNESS[@]}"
  fi

  echo ""
  echo "================================"
  echo "TOTAL FILES TO CONVERT: $TOTAL"
  echo "================================"
  echo ""
  echo "RECOMMENDATION: Convert in batches of 6-8 files per Claude Code session"
  echo ""
  echo "BATCH 1 (Facial - 3 files):"
  for file in "${FACIAL[@]}"; do
    echo "  pages/procedures/facial/$file"
  done
  echo ""

  echo "BATCH 2 (Body - 7 files):"
  for file in "${BODY[@]}"; do
    echo "  pages/procedures/body/$file"
  done
  echo ""

  echo "BATCH 3 (Hair + Pelvic Intimate - 10 files):"
  for file in "${HAIR[@]}"; do
    echo "  pages/procedures/hair/$file"
  done
  for file in "${PELVIC_INTIMATE[@]:0:2}"; do
    echo "  pages/procedures/pelvic-intimate/$file"
  done
  echo ""

  echo "Continue with remaining batches..."
  echo ""

} | tee -a $LOG_FILE

echo "Batch conversion guide created!"
echo "Log saved to: $LOG_FILE"
echo ""
echo "NEXT STEPS:"
echo "1. Copy the prompts above"
echo "2. Start new Claude Code session for each batch"
echo "3. Paste the batch prompt"
echo "4. Claude will convert those files"
echo ""
