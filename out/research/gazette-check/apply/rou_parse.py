import re,sys,json
FR,TO,OUT=sys.argv[1],sys.argv[2],sys.argv[3]
sys.argv=['gz.py']
exec(open('/tmp/claude-0/-home-user--github/bf61733e-4e03-51c3-9ac3-07a35af41a6a/scratchpad/gztool/gz.py').read().split("ap = argparse.ArgumentParser()")[0])
rows=[]
for r in records():
    if not (FR<=r['issue_date']<=TO): continue
    if 'Petroleum' not in r['ministry']: continue
    subj=r['subject']
    if not re.search(r'3\s*\(1\)|6\s*\(1\)|Right of User|ROU|RoU|PMP|Pipelines',subj,re.I): continue
    t=text_of(r) or ''
    k=t.find('MINISTRY OF PETROLEUM')
    e=t[k:] if k>=0 else t
    e1=re.sub(r'\s+',' ',e)
    sos=re.findall(r'(?:S\.\s?O\.|5\.\s?0\.|S\.\s?0\.|8\.0\.)\s?(\d{2,5})\s?\(E\)',e1)
    sec='6(1)' if re.search(r'sub-section \(1\) of section 6',e1) else ('3(1)' if re.search(r'sub-section \(1\) of section 3',e1) else '?')
    pipe=re.search(r'(?:for the transportation of|for transportation of)\s+(.{5,90}?)\s+(?:from|through|by)\s+(.{5,140}?)(?:,|\s+by\s+M/s|\s+in the State|\s+should|\s+and|\.)',e1)
    nm=re.findall(r'["“]([^"”]{8,120}(?:Pipeline|PIPELINE|pipeline|Project|Grid)[^"”]{0,60})["”]',e1)
    states=re.findall(r'State\s*[:\-]?\s*([A-Z][a-zA-Z ]{3,20})',e1)
    comp=re.search(r'(GAIL|Indian Oil|IOCL|Hindustan Petroleum|HPCL|Bharat Petroleum|BPCL|Indradhanush|IGGL|Numaligarh|ONGC|Oil India|Reliance|GSPL|Gujarat State|IHB|HPCL Rajasthan|HRRL|GIGL|Petronet|Mehsana)',e1)
    rows.append(dict(date=r['issue_date'],gid=r['gazette_id'],sos=sos[:6],sec=sec,pipe=(pipe.group(1)+' | '+pipe.group(2)) if pipe else '',names=nm[:2],states=sorted(set(states))[:4],comp=comp.group(1) if comp else '',url=r['gazette_source_url']))
json.dump(rows,open(OUT,'w'),ensure_ascii=False,indent=0)
print(len(rows))
