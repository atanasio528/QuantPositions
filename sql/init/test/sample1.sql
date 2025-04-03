-- 🧹 Clean up existing sample data (순서 중요: 자식 테이블 → 부모 테이블)
DELETE FROM applied;
DELETE FROM positions;
DELETE FROM companies;
DELETE FROM users;

-- 👤 Insert admin test user (yj2860)
INSERT INTO users (
    usrid, level, email, first_name, last_name, school, password_hash, created_at, updated_at, autho, cover_letter
) VALUES (
    'yj2860', 'NewGrad', 'yj2860@example.com', 'Youngjin', 'Jung', 'Columbia University',
    'fake_hash_here', '2025-03-30 19:24:09', '2025-03-30 19:24:09', 'admin', 'This is a generic cover letter.'
);

-- 👤 Insert test users (tester1, tester2)
INSERT INTO users (
    usrid, level, email, first_name, last_name, password_hash, autho
) VALUES
('tester1', 'NewGrad', 'tester1@example.com', 'Tester', 'One',
 '$2b$12$nRQ8tDvqPN9a9kUFb5K9gO83aEdWVKtBjoKH0SlZjRz0Kc9Ye3G9a', 'read'),
('tester2', 'NewGrad', 'tester2@example.com', 'Tester', 'Two',
 '$2b$12$VXRzjPdBOk1Gmk80qVtPvOCgT/5bdH62GMcYYpF.ZiAHtLMFK20RC', 'admin');

-- 🏢 Insert sample companies
INSERT INTO companies (cpid, cpname, industry, importance, headquarter, created_at, updated_at, updated_by)
VALUES
  ('CTDL', 'Citadel', 'HedgeFund', 1, '830 Brickell Plaza, Miami, FL 33131, USA', '2025-03-30', '2025-03-30', 'Youngjin'),
  ('CTDSEC', 'Citadel Securities', 'QuantTrading', 1, '830 Brickell Plaza, Miami, FL 33131, USA', '2025-03-30', '2025-03-30', 'Youngjin'),
  ('JANEST', 'Jane Street', 'QuantTrading', 1, '250 Vesey Street, New York, NY 10281, USA', '2025-03-30', '2025-03-30', 'Youngjin'),
  ('MILLEN', 'Millennium Management', 'HedgeFund', 1, '399 Park Avenue, New York, NY 10022, USA', '2025-03-30', '2025-03-30', 'Youngjin'),
  ('GLDMAN', 'Goldman Sachs', 'InvestmentBank', 1, '200 West Street, New York, NY 10282, USA', '2025-03-30', '2025-03-30', 'Youngjin'),
  ('JPMC', 'JPMorgan Chase', 'InvestmentBank', 1, '383 Madison Avenue, New York, NY 10179, USA', '2025-03-30', '2025-03-30', 'Youngjin'),
  ('BLROCK', 'BlackRock', 'AssetManagement', 1, '55 East 52nd Street, New York, NY 10055, USA', '2025-03-30', '2025-03-30', 'Youngjin'),
  ('FIDLTY', 'Fidelity', 'AssetManagement', 1, '245 Summer Street, Boston, MA 02210, USA', '2025-03-30', '2025-03-30', 'Youngjin'),
  ('SNPGLB', 'S&P Global', 'FinancialServices', 1, '55 Water Street, New York, NY 10041, USA', '2025-03-30', '2025-03-30', 'Youngjin'),
  ('CME', 'CME Group', 'Exchange', 1, '20 South Wacker Drive, Chicago, IL 60606, USA', '2025-03-30', '2025-03-30', 'Youngjin'),
  ('MOODYS', 'Moody''s', 'FinancialServices', 1, '7 World Trade Center, New York, NY 10007, USA', '2025-03-30', '2025-03-30', 'Youngjin'),
  ('ALLNZ', 'Allianz', 'Insurance', 1, 'Allianz SE, Königinstraße 28, 80802 Munich, Germany', '2025-03-30', '2025-03-30', 'Youngjin');

-- 💼 Insert sample positions
INSERT INTO positions (
    pztid, cpid, pztname, pztlevel, year, url, jd, note, active, deadline,
    updated_by, created_at, updated_at
) VALUES
('20250330_intern_1', 'CTDL', 'Quantitative Trading - Intern', 'Intern', 2025,
 'https://example.com/citadel2025intern1', 'JD', '', TRUE, '2025-05-01',
 'yj2860', '2025-03-30 19:24:09', '2025-03-30 19:24:09'),

('20250330_intern_2', 'CTDL', 'Trading Fundamental Analyst - Summer Intern', 'Intern', 2025,
 'https://example.com/citadel2025intern2', 'JD', '', TRUE, '2025-05-15',
 'yj2860', '2025-03-30 19:24:09', '2025-03-30 19:24:09'),

('20250330_newgrad_1', 'CTDL', 'Quantitative Research Analyst - Full Time', 'NewGrad', 2025,
 'https://example.com/citadel2025ft1', 'JD', '', TRUE, '2025-06-01',
 'yj2860', '2025-03-30 19:24:09', '2025-03-30 19:24:09'),

('20250330_intern_3', 'JPMC', 'Quantitative Research - Summer Associate', 'Intern', 2025,
 'https://example.com/jpm2025qa', 'JD', '', TRUE, '2025-04-30',
 'yj2860', '2025-03-30 19:24:09', '2025-03-30 19:24:09'),

('20250330_intern_4', 'JPMC', 'Quant Trader - Summer Associate', 'Intern', 2025,
 'https://example.com/jpm2025qt', 'JD', '', TRUE, '2025-05-10',
 'yj2860', '2025-03-30 19:24:09', '2025-03-30 19:24:09'),

('20250330_newgrad_2', 'JANEST', 'Quantitative Trader - Full Time', 'NewGrad', 2025,
 'https://example.com/janestreet2025ft', 'JD', 'Onsite Interview Required', TRUE, '2025-05-25',
 'yj2860', '2025-03-30 19:30:00', '2025-03-30 19:30:00'),

('20250330_associate_1', 'MILLEN', 'Quantitative Analyst - Associate', 'Associate', 2025,
 'https://example.com/millennium2025assoc', 'JD', '', TRUE, '2025-06-15',
 'yj2860', '2025-03-30 19:35:00', '2025-03-30 19:35:00'),

('20250330_intern_5', 'GLDMAN', 'Global Markets Intern', 'Intern', 2025,
 'https://example.com/gs2025intern', 'JD', 'Rotation across teams', TRUE, '2025-04-25',
 'yj2860', '2025-03-30 19:40:00', '2025-03-30 19:40:00'),

('20250330_newgrad_3', 'BLROCK', 'Quant Researcher - Entry Level', 'NewGrad', 2025,
 'https://example.com/blackrock2025newgrad', 'JD', '', TRUE, '2025-05-20',
 'yj2860', '2025-03-30 19:45:00', '2025-03-30 19:45:00'),

('20250330_vp_1', 'MOODYS', 'Risk Strategy Lead - VP', 'VP', 2025,
 'https://example.com/moodys2025vp', 'JD', 'Quant + Regulatory Experience required', FALSE, '2025-04-20',
 'yj2860', '2025-03-30 19:50:00', '2025-03-30 19:50:00');

-- 📄 Insert sample applied status
INSERT INTO applied (usrid, cpid, pztid, applied, applied_at) VALUES
('yj2860', 'CTDL', '20250330_intern_1', TRUE, '2025-03-30 20:00:00'),
('yj2860', 'CTDL', '20250330_intern_2', TRUE, '2025-03-30 20:00:00'),
('yj2860', 'CTDL', '20250330_newgrad_1', TRUE, '2025-03-30 20:00:00'),
('yj2860', 'JPMC', '20250330_intern_3', TRUE, '2025-03-30 20:00:00'),
('yj2860', 'JPMC', '20250330_intern_4', TRUE, '2025-03-30 20:00:00'),
('yj2860', 'JANEST', '20250330_newgrad_2', TRUE, '2025-03-30 21:00:00'),
('yj2860', 'MILLEN', '20250330_associate_1', FALSE, NULL),
('yj2860', 'GLDMAN', '20250330_intern_5', TRUE, '2025-03-30 21:05:00'),
('yj2860', 'BLROCK', '20250330_newgrad_3', TRUE, '2025-03-30 21:10:00'),
('yj2860', 'MOODYS', '20250330_vp_1', FALSE, NULL);
