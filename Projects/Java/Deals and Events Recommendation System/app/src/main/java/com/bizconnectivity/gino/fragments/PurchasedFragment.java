package com.bizconnectivity.gino.fragments;

import android.content.Context;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.design.widget.TabLayout;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentPagerAdapter;
import android.support.v4.view.ViewPager;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.LinearLayout;
import android.widget.TextView;

import com.bizconnectivity.gino.R;

import java.util.ArrayList;
import java.util.List;

import butterknife.BindView;
import butterknife.ButterKnife;

import static com.bizconnectivity.gino.Constant.SHARED_PREF_HISTORY_TAB;
import static com.bizconnectivity.gino.Constant.SHARED_PREF_KEY;
import static com.bizconnectivity.gino.Constant.TAB_AVAILABLE;
import static com.bizconnectivity.gino.Constant.TAB_HISTORY;

public class PurchasedFragment extends Fragment {

    @BindView(R.id.toolbar)
    Toolbar mToolbar;

    @BindView(R.id.tabLayout)
    TabLayout mTabLayout;

    @BindView(R.id.viewPager)
    ViewPager mViewPager;

    private SharedPreferences sharedPreferences;

    private int[] tabIcons = {
            R.drawable.ic_alarm_on_white_24dp,
            R.drawable.ic_history_white_24dp
    };

    public PurchasedFragment() {
        // Required empty public constructor
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        return inflater.inflate(R.layout.fragment_purchase, container, false);
    }

    @Override
    public void onViewCreated(View view, @Nullable Bundle savedInstanceState) {

        super.onViewCreated(view, savedInstanceState);

        // Layout Binding
        ButterKnife.bind(this, view);

        // Action Bar
        ((AppCompatActivity) getActivity()).setSupportActionBar(mToolbar);

        // Shared Preferences
        sharedPreferences = getContext().getSharedPreferences(SHARED_PREF_KEY, Context.MODE_PRIVATE);

        // View Pager
        setupViewPager(mViewPager);
        mTabLayout.setupWithViewPager(mViewPager);
        setupTabLayout();

        // Check Previous Tab Selected
        if (sharedPreferences.getBoolean(SHARED_PREF_HISTORY_TAB, false)) {
            if (mTabLayout != null) {
                SharedPreferences.Editor editor = sharedPreferences.edit();
                editor.putBoolean(SHARED_PREF_HISTORY_TAB, false).apply();
                mTabLayout.getTabAt(1).select();
            }
        }
    }

    private void setupTabLayout() {

        LinearLayout tabLinearLayout = (LinearLayout) LayoutInflater.from(getContext()).inflate(R.layout.custom_tab_two, null);
        LinearLayout tabLinearLayout2 = (LinearLayout) LayoutInflater.from(getContext()).inflate(R.layout.custom_tab_two, null);

        if (mTabLayout != null) {
            if (mTabLayout.getTabAt(0) != null) {

                TextView tabOne = (TextView) tabLinearLayout.findViewById(R.id.custom_tab_title);
                tabOne.setText(TAB_AVAILABLE);
                tabOne.setCompoundDrawablesWithIntrinsicBounds(tabIcons[0], 0, 0, 0);
                mTabLayout.getTabAt(0).setCustomView(tabOne);
            }

            if (mTabLayout.getTabAt(1) != null) {

                TextView tabTwo = (TextView) tabLinearLayout2.findViewById(R.id.custom_tab_title);
                tabTwo.setText(TAB_HISTORY);
                tabTwo.setCompoundDrawablesWithIntrinsicBounds(tabIcons[1], 0, 0, 0);
                mTabLayout.getTabAt(1).setCustomView(tabTwo);
            }
        }
    }

    private void setupViewPager(ViewPager viewPager) {

        ViewPagerAdapter adapter = new ViewPagerAdapter(getChildFragmentManager());

        adapter.addFragment(new AvailableFragment());
        adapter.addFragment(new HistoryFragment());

        viewPager.setAdapter(adapter);
    }

    class ViewPagerAdapter extends FragmentPagerAdapter {

        private final List<Fragment> mFragmentList = new ArrayList<>();

        ViewPagerAdapter(FragmentManager manager) {
            super(manager);
        }

        @Override
        public Fragment getItem(int position) {
            return mFragmentList.get(position);
        }

        @Override
        public int getCount() {
            return mFragmentList.size();
        }

        public void addFragment(Fragment fragment) {
            mFragmentList.add(fragment);
        }
    }

    @Override
    public void onResume(){
        super.onResume();
    }
}
